.. actex:: answer16_8_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Sorting
    :subchapter: Exercises
    :topics: Sorting/Exercises
    :from_source: T

    L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

    d = {}
    for x in L:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1

    s = sorted(d, key=lambda x: d[x], reverse=True)

    print(s[:5])