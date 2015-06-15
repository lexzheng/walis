Exception Definition
====================

Overall
-------

Walis has Four types of exception:

+----------------+------------+------------+--------------------------------------------------+
| Exception Name | Error code |  HTTP code |     Instruction                                  |
+================+============+============+==================================================+
|     DevExc     |    0 ~ 99  |     500    | Occurs when developing, should not exist on line |
+----------------+------------+------------+--------------------------------------------------+
|     SysExc     |  100 ~ 899 |     500    | System error,should not exist,including zeus     |
+----------------+------------+------------+--------------------------------------------------+
|    AuthExc     |  900 ~ 999 |     403    | No permission to access the API                  |
+----------------+------------+------------+--------------------------------------------------+
|    UserExc     | 10000 ~ INF|     400    | Caused by user, show this content on web page    |
+----------------+------------+------------+--------------------------------------------------+

Usage
-----

1. There are utils to raise exceptions in **walis.exception.util**

    a. raise_server_exc()
    b. raise_dev_exc()
    c. raise_auth_exc()
    d. raise_user_exc()

2. Raise corresponding exception inside API.

    1) without parameters

    .. code:: python

        raise_user_exc(SERVER_UNKNOWN_ERROR)

    2) with parameters

    .. code:: python

        raise_auth_exc(AUTH_FAILED_ERROR_TO_USER, user='maqic')

3. Other tips:

Mostly when we meet **business related error** or **user request error**, we should use raise_user_exc(),
for other system caused error such as **database error**, raise_server_exc().

Now the front end is able to deal with some situations and report err messages successfully,
and the situations have to contain HTTP code below 500(do not contain).
All the situations containing 500 code will be reported as sys err and no detail infomations.