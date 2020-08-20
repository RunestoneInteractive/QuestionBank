.. activecode:: cndtnlShortCircuit
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-shortCircuit
    :topics: 03-conditional/03-shortCircuit
    :from_source: T
    :caption: Errors from multiple conditionals

    x = 6
    y = 2
    print(x >= 2 and (x/y) > 2)

    x = 1
    y = 0
    print(x >= 2 and (x/y) > 2)

    x = 6
    y = 0
    print(x >= 2 and (x/y) > 2)