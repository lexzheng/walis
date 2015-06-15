.. _general:

Python Styles
=============

This section gives some example on what we prefer, it focus on the most common styles.

For more detailed coding style, refer to `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ and `Google Python Guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_.


Editor
------

Both Vim or PyCharm is OK, you have the choice.

Encoding
--------
Always add encoding declaration at top of python files.

The `#!` line is used by the kernel to find the Python interpreter, but is ignored by Python when importing modules.

For scripts which will be executed, add this:

.. code:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

For modules / packages which will not be executed directly, only add this:

.. code:: python

    # -*- coding: utf-8 -*-

Unicode
-------

Use unicode as standard.

Accept unicode as param in function and return unicode string too.


Main function
-------------

For python scripts which need to be run in shell, use main function to do the jobs.

Don't directly execute any code. Put everything inside main function.

.. code:: python

    def main():
        # do tasks
        pass

    if __name__ == '__main__':
        main()

And for all module files, don't add ``if main`` things there. Module files are not meant to be executed directly and they may contain relative imports which prevent it from running directly.

If you need tests, write tests. Don't add tests to ``if main``.


Imports
-------

Import one module per line.

Yes

.. code:: python

    import time
    import datetime

No

.. code:: python

    import time, datetime

Import multiple module from one package using `()` with 4 spaces indentation.

Yes

.. code:: python

    from zeus.sms.models import (
        DBSession,
        ShortMessageSend,
    )

No

.. code:: python

    from zeus.sms.models import DBSession
    from zeus.sms.models import ShortMessageSend

Use `from x import y as z` if two modules named y are to be imported or if y is an inconveniently long name.

Yes

.. code:: python

    from zeus.sms.client import client as sms_client
    from zeus.ers.client import client as ers_client

Import build-in modules first, then third party modules, then project modules, then parent directory relative modules, then current directory relative modules.

Yes

.. code:: python

    import datetime
    import logging

    from sqlalchemy.exc import SQLAlchemyError
    from thrift.Thrift import TException

    from zeus.core.decorators import memoize
    from zeus.ers.client import client as ers_client

    from ..messager.exc import MessagerError

    from . import messager


Line length
-----------
Limit all lines to a maximum of 79 characters.

The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses.

Yes

.. code:: python

    class Rectangle(Blob):

        def __init__(self, width, height,
                     color='black', emphasis=None, highlight=0):
            if (width == 0 and height == 0 and
                    color == 'red' and emphasis == 'strong' or
                    highlight > 100):
                raise ValueError("sorry, you lose")
            if width == 0 and height == 0 and (color == 'red' or
                                               emphasis is None):
                raise ValueError("I don't think so -- values are %s, %s" %
                                 (width, height))
            Blob.__init__(self, width, height,
                          color, emphasis, highlight)


Indentation
-----------

Indent your code blocks with 4 spaces.

Yes

.. code:: python

    # Aligned with opening delimiter
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

    # 4-space hanging indent; nothing on first line
    foo = long_function_name(
        var_one, var_two, var_three, var_four)

    # More indentation included to distinguish this from the rest.
    def long_function_name(
            var_one, var_two, var_three, var_four):
        print(var_one)

No

.. code:: python

    # Arguments on first line forbidden when not using vertical alignment
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # 2-space hanging indent forbidden
    foo = long_function_name(
      var_one, var_two, var_three,
      var_four)


    # Further indentation required as indentation is not distinguishable
    def long_function_name(
        var_one, var_two, var_three, var_four):
        print(var_one)

    # Don't use indentation when not necessary
    foo = long_function_name(
        var_one, var_two)

Whitespace
----------
No whitespace inside parentheses, brackets or braces.

Yes

.. code:: python

    spam(ham[1], {eggs: 2}, [])

No

.. code:: python

    spam( ham[ 1 ], { eggs: 2 }, [ ] )

No whitespace before a comma, semicolon, or colon. Do use whitespace after a comma, semicolon, or colon except at the end of the line.

Yes

.. code:: python

    if x == 4:
        print x, y

No

.. code:: python

    if x == 4 :
        print x , y

Don't use spaces around the '=' sign when used to indicate a keyword argument or a default parameter value.

Yes

.. code:: python

    def complex(real, imag=0.0):
        return magic(r=real, i=imag)

No

.. code:: python

    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)

Don't use spaces to vertically align tokens on consecutive lines, since it becomes a maintenance burden (applies to :, #, =, etc.):

Yes

.. code:: python

    foo = 1000  # comment
    long_name = 2  # comment that should not be aligned

    dictionary = {
        "foo": 1,
        "long_name": 2,
    }

No

.. code:: python

    foo       = 1000  # comment
    long_name = 2     # comment that should not be aligned

    dictionary = {
        "foo"      : 1,
        "long_name": 2,
    }


Ternary Operator
----------------

Use ternary operator for simple statements.

Yes

.. code:: python

    a = b if b > 3 else 3

No

.. code:: python

    if b > 3:
        a = b
    else:
        a = 3

Sometimes you can simply use ``or`` clause.

Yes

.. code:: python

    a = b or ""

No

.. code:: python

    a = b if b else ""

    if b:
        a = b
    else:
        a = ""


Comparison
----------

Make it simple.

Yes

.. code:: python

    if 1 < x < 3:
        print True

    if 1 < x > 0:
        print True

    if a == b == c:
        print True

No

.. code:: python

    if 1 < x and x < 3:
        print True

    if 1 < x and x > 0:
        print True

    if a == b and a == c:
        print True


Use ``in`` for multiple or compare.

Yes

.. code:: python

    if a in [CONST_A, CONST_B]:
        print True

No

.. code:: python

    if a == CONST_A or a == CONST_B:
        print True


Strings
-------

Use `+` to combine 2 strings and use ``format`` to formatting string in a more complex situation.

Yes

.. code:: python

    # combine 2 strings
    x = a + b

    # simple format
    x = "{0}/{1}".format(a, b)

    # params format
    params = {
        "host": HOST,
        "port": PORT
    }
    x = "{host}:{port}".format(**params)


No

.. code:: python

    # use `+` or format
    x = '%s%s' % (a, b)

    # don't use `+` for more than 2 strings
    x = imperative + ', ' + expletive + '!'

    # use format for complex string format
    x = 'name: %s; score: %d' % (name, n)

Avoid using the + and += operators to accumulate a string within a loop. Since strings are immutable, this creates unnecessary temporary objects and results in quadratic rather than linear running time. Instead, add each substring to a list and ``''.join`` the list after the loop terminates.

Yes

.. code:: python

    for e in extras:
        e_strs.append(u"{name}{quantity}份{price}元".format(**e))
    extras_desc = u'/'.join(e_strs)

No

.. code:: python

    # don't use '%s' format
    for e in extras:
        e_strs.append(u"%s%s份%s元" % (e['name'], e['quantity'], e['price']))
    extras_desc = u'/'.join(e_strs)

    # don't use += to build string
    extras_desc = ""
    for e in extras:
        extras_desc += u"/{name}{quantity}份{price}元".format(**e)


List Operation
--------------

Iterate through list:

.. code:: python

    x = [1, 2, 3, 4, 5, 6]
    for i in x:
        print i

Iterate through list with an index:

Yes

.. code:: python

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams):
        print index, team

No

.. code:: python

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for i in range(len(teams)):
        print i, teams[i]

Slice list:

.. code:: python

    >>> x = [1, 2, 3, 4, 5, 6]

    >>> print x[:3]
        [1,2,3]

    >>> print x[1:5]
        [2,3,4,5]

    >>> print x[-3:]
        [4,5,6]

    >>> print x[::2]
        [1,3,5]

    >>> print x[1::2]
        [2,4,6]


List Comprehension
------------------

Use list comprehension to make code simple:

Yes

.. code:: python

    numbers = [1, 2, 3, 4, 5, 6]
    even = [i for i in numbers if i % 2 == 0]

No

.. code:: python

    numbers = [1,2,3,4,5,6]
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)


But, only use list comprehensions in simple and clean situation:

Yes

.. code:: python

    msg_ids = [msg.id for msg in msgs]

No

.. code:: python

    result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]


Dict Operation
--------------

Get item from dict

Yes

.. code:: python

    data = {'user': 1, 'name': 'Max', 'three': 4}
    is_admin = data.get('admin', False)

No

.. code:: python

    data = {'user': 1, 'name': 'Max', 'three': 4}
    try:
        is_admin = data['admin']
    except KeyError:
        is_admin = False

Use default iterators and operators for types that support them.

Yes

.. code:: python

    if key in adict:
        ...

    for key in adict:
        ...

    for k, v in adict.iteritems():
        ...

No

.. code:: python

    if adict.has_key(key):
        ...

    for key in adict.keys():
        ...

    for k, v in adict.items():
        ...


Dict Comprehension
------------------

Dict comprehensions are just like list comprehensions, except that you group the expression using curly braces instead of square braces.

Yes

.. code:: python

    d = {i : chr(65 + i) for i in range(4)}

No

.. code:: python

    d = {}
    for i in range(4):
        d[i] = chr(65 + i)


Generators
----------

Generator is good, it save you from creating temporary lists and thereby both save memory and simplify the code.

Yes

.. code:: python

    def combinations(starters, endings):
        for s in starters:
            for e in endings:
                yield s + e

NO

.. code:: python

    def combinations(starters, endings):
        result = []
        for s in starters:
            for e in endings:
                result.append(s + e)
        return result

For functions that support generators such as ``sum``, ``join``, ``sorted``, directly use generators.

Yes

.. code:: python

    sum(x * x for x in range(2000000))
    ' '.join(c for c in "Hello World!")

No

.. code:: python

    sum([x * x for x in range(2000000)])
    ' '.join([c for c in "Hello World!"])


This also applies to file operation.

Yes

.. code:: python

    with open('file.txt', 'r') as f:
        for line in f:
            ...

No

.. code:: python

    with open('file.txt', 'r') as f:
        for line in f.readlines():
            ...


Context Manager
---------------

Try to make use of context manager when to deal with resource allocation. The code will be much clearer and easier to understand, and it ensure the resources released at exit.

A common example is open file.

Yes

.. code:: python

    with open('/tmp/file', 'w') as f:
        f.write('sometext')

No

.. code:: python

    f = open('/tmp/file', 'w')
    try:
        n = f.write('sometext')
    finally:
        f.close()


Collections and Itertools
-------------------------

``collections`` and ``itertools`` are powerful, use them wisely.

.. code:: python

    >>> import collections

    >>> c = collections.Counter()
    >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    ... c[word] += 1
    ...
    >>> c
    Counter({'blue': 3, 'red': 2, 'green': 1})

    >>> c = collections.Counter("hello")
    >>> c
    Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

    >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    >>> d = collections.defaultdict(list)
    >>> for k, v in s:
    ...     d[k].append(v)
    ...
    >>> d.items()
    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


    >>> import itertools

    >>> for p in itertools.permutations("abc"):
    ...     print p
    [('a', 'b', 'c'),
     ('a', 'c', 'b'),
     ('b', 'a', 'c'),
     ('b', 'c', 'a'),
     ('c', 'a', 'b'),
     ('c', 'b', 'a')]

    >>> teams = ["Packers", "49ers", "Ravens", "Patriots"]
    >>> for game in itertools.combinations(teams, 2):
    ...     print game
    ('Packers', '49ers')
    ('Packers', 'Ravens')
    ('Packers', 'Patriots')
    ('49ers', 'Ravens')
    ('49ers', 'Patriots')
    ('Ravens', 'Patriots')



Default Argument Values
-----------------------

Do not use mutable objects as default values in the function or method definition.

Yes

.. code:: python

    def foo(a, b=None):
        b = b or []

No

.. code:: python

    def foo(a, b=[])

Calling code must use named values for arguments with a default value. This helps document the code somewhat and helps prevent and detect interface breakage when more arguments are added.

Yes

.. code:: python

    def foo(a, b=1):
        ...

    foo(1)
    foo(1, b=2)

No

.. code:: python

    foo(1, 2)


Properties
----------

Use properties directly, don't use accessor or setter methods.

Yes

.. code:: python

    class A(object):
        length = 2
        width = 3

    a = A()
    a.length = 5
    a.width = 6

No

.. code:: python

    class A(object):
        length = 2
        width = 3

        def set_length(self, length):
            self.length = length

        def set_width(self, width):
            self.width = width

    a = A()
    a.set_length(5)
    a.set_width(6)


Create read-only properties with the @property decorator.

Yes

.. code:: python

    class A(object):
        length = 2
        width = 3

        def area(self):
            return self.length * self.width

    a = A()
    a.aera()

    # This is preferred
    class A(object):
        length = 2
        width = 3

        @property
        def area(self):
            return self.length * self.width

    a = A()
    a.area


True/False evaluations
----------------------

`0`, `None`, `[]`, `{}`, `""` all evaluate as `False` in a boolean context.

Yes

.. code:: python

    if foo:
        ...

    if not seq:
        ...

    if foo is None:
        ...

No

.. code:: python

    if foo is True:
        ...

    if len(seq) == 0:
        ...

    if foo == None:
        ...


Type compare
------------

Object type comparisons should always use isinstance() instead of comparing types directly.

Yes

.. code:: python

    if isinstance(obj, int):
        ...

No

.. code:: python

    if type(obj) is int:
        ...

Use `basestring` to check if something is string. Cause `basestring` includes both `str` and `unicode`.

.. code:: python

    >>> isinstance("abc", str)
    True

    >>> isinstance(u"abc", str)
    False

    >>> isinstance("abc", basestring)
    True

    >>> isinstance(u"abc", basestring)
    True


Error handling
--------------

Be **explicit** about error.

Only deal with the exception you know. Never surround block of code by
``Exception``, use detailed exception instead.

Yes

.. code-block:: python

    def some_function(num):
        try:
            return 1 / num
        except ZeroDivisionError:
            print "num should not be zero"

No

.. code-block:: python

    def some_function(num):
        try:
            a = 1 / num
        except Exception as e:
            logging.exception(e)

And surround ``try..except`` to as few lines as possible.

Yes

.. code:: python

    def some_function(*args):
        session = DBSession()
        session.add(obj)

        try:
            session.commit()
        except SQLAlchemyError as se:
            session.revoke()

        return "hello"

No

.. code:: python

    def some_function(*args):
        try:
            session = DBSession()
            session.add(obj)
            session.commit()
            return "hello"
        except SQLAlchemyError as se:
            session.revoke()
