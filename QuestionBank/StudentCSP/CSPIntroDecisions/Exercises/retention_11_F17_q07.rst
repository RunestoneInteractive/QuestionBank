.. mchoice:: retention_11_F17_q07
    :author: Barbara  Ericson
    :difficulty: 1.0
    :basecourse: StudentCSP
    :chapter: CSPIntroDecisions
    :subchapter: Exercises
    :topics: CSPIntroDecisions/Exercises
    :from_source: F
    :practice: T

    What will the following code print out?

    .. sourcecode:: python

        def enum(L):
            return zip(range(len(L)), L)

        print (enum(['a', 'b', 'c']))

    ..

    -   [(1, 'a'), (2, 'b'), (3, 'c')]

        -   Incorrect!

    -   <type 'float'>

        -   Incorrect!

    -   [(0, 'a'), (1, 'b'), (2, 'c')]

        +   Correct!

    -   [(3, 'a'), (3, 'b'), (3, 'c')]

        -   Incorrect!

    -   [('a', 'a'), ('b', 'b'), ('c', 'c')]

        -   Incorrect!

    -   [('a'), ('b'), ('c')]

        -   Incorrect!

    -   None

        -   Incorrect!

    -   No output; there is an error

        -   Incorrect!