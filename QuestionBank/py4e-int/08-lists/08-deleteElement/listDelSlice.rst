.. activecode:: listDelSlice
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-deleteElement
    :topics: 08-lists/08-deleteElement
    :from_source: T
    :caption: Using del with a slice to remove multiple list elements.

    t = ['a', 'b', 'c', 'd', 'e', 'f']
    del t[1:5]
    print(t)