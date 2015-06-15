# coding=utf8

from __future__ import absolute_import, division, print_function


from walis.thirdparty import (
    thrift_client,
    thirdparty_svc,
)
from walis.utils.misc import (
    any_to_dic,
    any_to_raw,
)


def query_regions(region_ids=None, city_ids=None, type_codes=None, search=None,
                  show_all=None):
    """

    :param region_ids:
    :param city_ids:
    :param type_codes: {CBD:1, SCHOOL:2}
    :param search: search by region_name
    :param show_all: whether show regions whose id < 0
    :return:
    """
    query = thirdparty_svc.ers.TRegionQuery()
    query.search = search
    query.show_all = show_all
    query.city_ids = city_ids
    query.region_ids = region_ids
    query.type_codes = type_codes

    with thrift_client('ers') as ers:
        result = ers.query_region(query)

    result = any_to_raw(result)
    result = any_to_dic(result)
    return result
