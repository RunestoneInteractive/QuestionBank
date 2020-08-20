.. activecode:: listEmptyLoop
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-traversing
    :topics: 08-lists/08-traversing
    :from_source: T
    :caption: Trying to iterate through an empty list.

    empty = []
    for x in empty:
        print('This never happens.')