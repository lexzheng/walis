# coding=utf8

from __future__ import absolute_import, division, print_function
from walis.service.region import region
from walis.service.rst.inner import query_all_rsts, update_restaurant_region


def main():
    rsts = query_all_rsts(city_ids=[1], is_valid=1, is_premium=0)
    rst_region_map = region.get_region_map_by_rst([rst['id'] for rst in rsts])
    region_map = region.mget(list(set(rst_region_map.values())), return_map=True)
    unregioned_count = 0
    unregions = []

    for rst_id, region_id in rst_region_map.iteritems():
        if not region_map.has_key(region_id):
            unregioned_count += 1
            print('{}, {}'.format(rst_id, region_id))
            unregions.append(region_id)
            update_restaurant_region(rst_id, -10)

    print('total unregioned: {}'.format(unregioned_count))
    print('unregions: {}'.format(list(set(unregions))))


if __name__ == '__main__':
    main()
