.. activecode::  cndtnl-wc-pay2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T

    Rewrite your pay program using ``try`` and ``except`` so that your program handles non-numeric
    input gracefully by printing a message and exiting the program. The following shows two
    executions of the program:

    .. code-block::

        Enter Hours: 20
        Enter Rate: nine
        Error, please enter numeric input


    .. code-block::

        Enter Hours: forty
        Error, please enter numeric input

    ~~~~