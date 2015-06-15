#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import arrow

from walis.utils.misc import ttype2dict
from . import inner as base


def query(city_ids, activity_category_id=None, restaurant_ids=None, status=None,
          created_at_from=arrow.now().replace(days=-8).timestamp,
          offset=None, limit=None):
    condition = base.create_contract_query_condition(
        city_ids=city_ids,
        activity_category_id=activity_category_id,
        restaurant_ids=restaurant_ids,
        status=status,
        created_at_from=created_at_from,
        offset=offset,
        limit=limit
    )
    contract_list = base.query_contract(condition)
    contract_list = [ttype2dict(ct) for ct in contract_list]
    contract_count = base.count_contract(condition)
    return {"count": contract_count, "contracts": contract_list}
