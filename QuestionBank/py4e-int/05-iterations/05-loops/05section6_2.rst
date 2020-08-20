.. activecode:: 05section6_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-loops
    :topics: 05-iterations/05-loops
    :from_source: T
    :coach:
    :caption: To find the smallest value in a list or sequence, we construct the following loop.

    smallest = None
    print('Before:', smallest)
    for itervar in [3, 41, 12, 9, 74, 15]:
        if smallest is None or itervar < smallest:
            smallest = itervar
        print('Loop:', itervar, smallest)
    print('Smallest:', smallest)