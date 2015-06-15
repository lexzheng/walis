# coding=utf8

from __future__ import absolute_import, division, print_function

MAX_LIMIT_SIZE = 1000


def query_all(func, offset=0, per_limit=MAX_LIMIT_SIZE, *args, **kwargs):
    results = []
    kwargs.update(offset=offset, limit=per_limit)

    while True:
        per_results = func(*args, **kwargs)

        if not per_results or len(per_results) == 0:
            break

        results.extend(per_results)

        per_limit = len(per_results)
        offset += per_limit
        kwargs.update(offset=offset, limit=per_limit)

    return results
