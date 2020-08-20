.. codelens:: chp09_is4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: CloningLists
    :topics: Lists/CloningLists
    :from_source: T
    :showoutput:

    a = [81, 82, 83]

    b = a[:]       # make a clone using slice
    print(a == b)
    print(a is b)

    b[0] = 5

    print(a)
    print(b)