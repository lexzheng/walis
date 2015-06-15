# coding=utf8

from walis import config
from walis.core.app import WalisApp


app = WalisApp(__name__)
app.init(config)


if __name__ == '__main__':
    # print all supported api
    from pprint import pprint as pp
    from operator import attrgetter
    rule_list = list(app.url_map.iter_rules())
    rule_list.sort(key=attrgetter('rule'))
    pp(rule_list)

    app.run(host='0.0.0.0', port=17007, debug=False)
