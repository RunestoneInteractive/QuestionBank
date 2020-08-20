.. activecode:: clens8_5_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: CloningLists
    :topics: TransformingSequences/CloningLists
    :from_source: T

    a = [81,82,83]

    b = a[:]       # make a clone using slice
    print(a == b)
    print(a is b)

    b[0] = 5

    print(a)
    print(b)