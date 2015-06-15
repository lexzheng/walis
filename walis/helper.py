# coding=utf8
import argparse
from walis.thrift.client import jvs_client


def helper():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="api/thrift")
    parser.add_argument("--host", help="listen host")
    parser.add_argument("--port", help="listen port")
    parser.add_argument("-r", "--real", action="store_true",
                        help="force use real client")
    args = parser.parse_args()

    if args.name == 'thrift' or args.name == 't':
        _thrift_helper()
    elif args.name == 'api' or args.name == '':
        _api_helper()


# TODO fix transport close bug
def _thrift_helper():
    with jvs_client() as c:
        c.ping()
        import IPython
        IPython.embed()


def _api_helper():
    from walis.server import app
    c = app.test_client()  # noqa
    import IPython
    IPython.embed()


if __name__ == '__main__':
    helper()
