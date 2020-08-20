.. mchoice:: vars_types_3
    :author: bmiller
    :difficulty: 3
    :basecourse: thinkcpp
    :topics: Chapter2/exercises
    :from_source: T

    What is the value of ``x``?

    ::

        x = 2 + (13 - 5) * 2 + 6 /3;

    -   7

        -   ``13 - 5`` is computed first because it is in parentheses.

    -   20

        +   C++ follows the order of operations.

    -   23.333

        -   ``2 + 6`` is not grouped together like ``13 - 5``.

    -   34

        -   ``2 + 6 / 3`` is not computed first.