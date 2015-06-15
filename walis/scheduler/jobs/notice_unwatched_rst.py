#! /usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import print_function, division, absolute_import

import logging
from collections import defaultdict

from walis.scheduler.jobs import job_deco
from walis.service.rst import (
    director as rst_dir_base,
    restaurant as rst_base
)
from walis.service.region import (
    region as region_base,
    region_group as region_group_base,
)
from walis.service.user import user as user_base
from walis.service.utils import email as email_base

log = logging.getLogger('scheduler.restaurant.notice_unwatched_rst')

EMAIL_TITLE = u'您负责区域下还有未设置市场责任人的餐厅'

URL = u"http://javis.ele.me/restaurant/receipt"

TABLE_TITLE = u'你负责的区域内以下餐厅还未设置市场负责人，请安排相关人员到 <a href="{0}">{1}</a> 页面进行设置'\
    .format(URL, URL)

HTML = u'''<html><head>
    <meta charset="utf-8">
    </head><body>
    <h3>{title}</h3>
    <table class='table table-striped'>
    <thead>{table_head}</thead>
    <tbody>{table_body}</tbody>
    </table>
    <div>{memo}</div>
    </body></html>'''

TABLE_HEAD = u'<tr><th>%-11s</th><th>%-20s</th></tr>' % (u'餐厅ID', u'餐厅名称')

MEMO = u'''
    <h3>附:市场负责人说明及注意事项</h3>
    <p>后台餐厅市场负责人的显示按照在该页面<a href="{url}">{url}</a>的勾选进行显示，即：市场经理勾选了该餐厅，在餐厅详情页即会显示该市场经理联系方式。请区域负责人安排相关人员进行勾选。</p>
    <p>注意事项：</p>
    <p>1、如果市场经理被去除某个区域权限，第二天该区域内相关餐厅市场负责人将不显示该市场经理</p>
    <p>2、如果市场经理被加上某个区域权限，需要市场经理自己去<a href="{url}">{url}</a>勾选，才会在餐厅页显示该市场经理的信息。</p>
    <p>3、市场经理每新建一家餐厅后需到<a href="{url}">{url}</a>勾选才能将接收相关短信。</p>
    '''.format(url=URL)

MAX_LIMIT = 1000


@job_deco
def notice_unwatched_rst():
    """
    email to director which restaurant don't has director
    """
    not_director_rst_dict = _get_not_director_rst()

    regroup_dict = _get_regroup_dict(not_director_rst_dict)

    _set_user_to_regroup_dict(regroup_dict)

    _send_by_area(regroup_dict)


def _get_all_rst_dict():
    rst_dict = {}
    offset = 0
    limit = MAX_LIMIT
    while 1:
        rsts = rst_base.query_restaurant(is_valid=1,
                                         is_premium=0,
                                         offset=offset,
                                         limit=limit)
        tmp_rst_dict =\
            {int(rst['_id']): {'rst_id': int(rst['_id']),
                      'name': rst['_source']['name'],
                      'city_id': int(rst['_source']['city_id'])} for rst in rsts}
        rst_dict.update(tmp_rst_dict)
        offset += limit
        if len(rsts) < limit:
            break
    return rst_dict


def _get_all_dir_rst_ids():
    limit = MAX_LIMIT
    offset = 0
    all_dir_rst_ids = set()
    while 1:
        rst_dirs = rst_dir_base\
            .query_restaurant_director(limit=limit, offset=offset, in_charge=1)
        offset += limit
        all_dir_rst_ids.update(set([rst_dir.restaurant_id for rst_dir in rst_dirs]))
        if len(rst_dirs) < limit:
            break
    return all_dir_rst_ids


def _get_not_director_rst():
    rst_dict = _get_all_rst_dict()
    rst_ids = rst_dict.keys()
    all_dir_rst_ids = _get_all_dir_rst_ids()
    not_director_rst_ids = _diff(rst_ids, all_dir_rst_ids)
    not_director_rst_dict = {k: rst_dict[k] for k in not_director_rst_ids}
    log.info("The total count of rst:%s" % (len(not_director_rst_ids)))
    return not_director_rst_dict


def _set_region_to_rst(rst_dict):
    rst_to_region_map = region_base.get_region_map_by_rst(rst_dict.keys())
    region_ids = rst_to_region_map.values()
    region_to_region_group_map = \
        region_group_base.get_region_group_map_by_region(region_ids)
    for rst_id, rst in rst_dict.iteritems():
        if rst_to_region_map.get(rst_id) is not None:
            region_id = rst_to_region_map.get(rst_id)
            rst['region_id'] = region_id
            if region_to_region_group_map.get(region_id) is not None:
                rst['region_group_id'] = region_to_region_group_map.get(region_id)
            else:
                log.warning(u"region<{}>: could not find region_group.".format(region_id))
        else:
            log.warning(u"rst<{}>: could not find region.".format(rst_id))


def _get_regroup_dict(not_director_rst_dict):
    _set_region_to_rst(not_director_rst_dict)

    regroup_dict = {'region_group': defaultdict(list),
                    'region': defaultdict(list)}
    for rst_id, rst in not_director_rst_dict.iteritems():
        if rst.get('region_group_id') is not None:
            regroup_dict['region_group'][rst['region_group_id']].append(rst)
        if rst.get('region_id') is not None:
            regroup_dict['region'][rst['region_id']].append(rst)

    return regroup_dict


def _set_user_to_regroup_dict(regroup_dict):

    regions = regroup_dict['region']
    region_groups = regroup_dict['region_group']

    region_group_user_email = defaultdict(set)
    for region_group_id in region_groups:
        user_ids = user_base.get_director_ids_by_area(region_group_ids=[region_group_id, ])
        profiles = user_base.mget_profile(user_ids)
        region_group_user_email[region_group_id].update(set([profile.email for profile in profiles]))

    region_user_email = defaultdict(set)
    for region_id in regions:
        user_ids = user_base.get_director_ids_by_area(region_ids=[region_id, ])
        profiles = user_base.mget_profile(user_ids)
        region_user_email[region_id].update(set([profile.email for profile in profiles]))

    # 重组
    for region_group_id, rst_list in region_groups.iteritems():
        region_groups[region_group_id] = {
            "rst_list": rst_list,
            "email_list": region_group_user_email.get(region_group_id)
        }
    for region_id, rst_list in regions.iteritems():
        regions[region_id] = {
            "rst_list": rst_list,
            "email_list": region_user_email.get(region_id)
        }


def _create_content(rst_list):

    table_body = u''
    end_str = u''
    if len(rst_list) > 30:
        rst_list = rst_list[:30]
        end_str = u'...'
    for rst in rst_list:
        table_body += u'<tr><td>%-11s</td><td><a href="http://walle.ele.me/restaurant/dashboard?id=%s">%-20s</a></td></tr>\n'\
                      % (rst['rst_id'], rst['rst_id'], rst['name'])
    table_body += u'<tr><td>{0}<td/><td></td></tr>'.format(end_str)
    html = HTML.format(title=TABLE_TITLE, table_head=TABLE_HEAD, table_body=table_body, memo=MEMO)
    return html


def _send_by_area(regroup_dict):
    for area_name, areas in regroup_dict.iteritems():
        for area_id, area_item in areas.iteritems():
            if not area_item['email_list']:
                log.warning(u"\n{0}<{1}>: could not find director.\nrst_ids:\n{2}"
                            .format(area_name, area_id, [rst['rst_id'] for rst in area_item['rst_list']]))
                continue

            email_base.msend('no-reply@mail.ele.me',
                             area_item['email_list'],
                             EMAIL_TITLE,
                             _create_content(area_item['rst_list']))
            log.info(u"\nsend email to:\n{0}\nrst_ids:\n{1}"
                     .format(area_item['email_list'],[rst['rst_id'] for rst in area_item['rst_list']]))


def _diff(list1, list2):
    if not list1 or not list2:
        return list1
    return set(list1) - set(list2)


if __name__ == "__main__":
    notice_unwatched_rst()
