.. codelens:: chp09_is3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Aliasing
    :topics: Lists/Aliasing
    :from_source: T
    :showoutput:

    a = [81, 82, 83]
    b = [81, 82, 83]

    print(a == b)
    print(a is b)

    b = a
    print(a == b)
    print(a is b)

    b[0] = 5
    print(a)