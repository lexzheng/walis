.. _style:

Coding Style
============

This section talks about common coding style in zeus.

Firstly, let's go through the guidelines:

.. code:: python

    >>> import this

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


Secondly, be consistent. Here's a quote from google python guide.

::

    BE CONSISTENT.

    If you're editing code, take a few minutes to look at the code around you
    and determine its style. If they use spaces around all their arithmetic
    operators, you should too. If their comments have little boxes of hash
    marks around them, make your comments have little boxes of hash marks
    around them too.

    The point of having style guidelines is to have a common vocabulary of
    coding so people can concentrate on what you're saying rather than on how
    you're saying it. We present global style rules here so people know the
    vocabulary, but local style is also important. If code you add to a file
    looks drastically different from the existing code around it, it throws
    readers out of their rhythm when they go to read it. Avoid this.

There're some small differs between PEP8, google style and zeus coding style, and coding styles may change by time. But we all follow the zeus rules in this documentation when style differs.


.. toctree::
    :maxdepth: 2

    style/python