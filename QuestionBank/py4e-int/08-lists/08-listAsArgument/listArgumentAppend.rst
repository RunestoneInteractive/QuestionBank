.. activecode:: listArgumentAppend
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listAsArgument
    :topics: 08-lists/08-listAsArgument
    :from_source: T
    :caption: Using append method and the + operator with lists.

    t1 = [1, 2]
    t2 = t1.append(3)
    print(t1)
    print(t2)

    t3 = t1 + [3]
    print(t3)
    print(t2 is t3)