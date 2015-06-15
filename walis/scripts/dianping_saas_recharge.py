# coding=utf8

from __future__ import absolute_import, division, print_function
import json
from walis.service.rst.inner import query_all_rsts
from walis.thirdparty import thrift_client

city_id = 1
recharge_day = 30
change_attr_remains = 1
system_user_id = -1

SAAS_STATUS_SUSPEND = 0  # 停用
SAAS_STATUS_FREE = 1  # 免费试用
SAAS_STATUS_TRIAL = 2  # 需付费
SAAS_STATUS_PAY = 3  # 已付费
SAAS_STATUS_TEMP_FREE = 4  # 暂不收费


def get_restaurants(city_id, saas_statuses):
    rsts = query_all_rsts(city_ids=[city_id],
                          is_valid=1,
                          has_dianping_id=True,
                          saas_statuses=saas_statuses,
                          )
    print('total rsts: {}'.format(len(rsts)))
    return [r['id'] for r in rsts]


def change_saas_status(rst_ids, saas_status):
    for rst_id in rst_ids:
        try:
            with thrift_client('ers') as ers:
                ers.saas_set_status_custom(
                    rst_id,
                    saas_status,
                    '',
                    system_user_id,
                )
        except:
            print('change saas status exc: {}'.format(rst_id))
            continue


# def recharge_saas_for_days(rst_ids):
# for rst_id in rst_ids:
#         try:
#             with thrift_client('ers') as ers:
#                 ers.saas_recharge_custom(
#                     rst_id,
#                     change_attr_remains,
#                     recharge_day,
#                     system_user_id,
#                     ''
#                 )
#         except:
#             print('exc: {}'.format(rst_id))
#             continue


def recharge_saas_to_date(rst_ids, date):
    for rst_id in rst_ids:
        try:
            with thrift_client('ers') as ers:
                ers.saas_set_temp_free(
                    rst_id,
                    date,
                    '',
                    system_user_id,
                )

        except:
            print('rechage saas exc: {}'.format(rst_id))
            continue


def main():
    rst_ids = get_restaurants(city_id,
                              [SAAS_STATUS_SUSPEND, SAAS_STATUS_TRIAL])
    change_saas_status(rst_ids, SAAS_STATUS_TEMP_FREE)

    rst_ids2 = get_restaurants(city_id, [SAAS_STATUS_TEMP_FREE])
    recharge_saas_to_date(rst_ids2, '2015-4-18')


if __name__ == '__main__':
    main()
