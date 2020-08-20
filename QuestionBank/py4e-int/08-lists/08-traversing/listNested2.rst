.. activecode:: listNested2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-traversing
    :topics: 08-lists/08-traversing
    :from_source: T
    :caption: Lists within lists only count as one element for the original list.

    bigList = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
    print(len(bigList))