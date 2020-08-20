.. codelens:: cl_chp09_is4
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: CloningLists
    :topics: Lists/CloningLists
    :from_source: None
    :showoutput:

    a = [81, 82, 83]

    b = a[:]       # make a clone using slice
    print(a == b)
    print(a is b)

    b[0] = 5

    print(a)
    print(b)