.. codelens:: search2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheSequentialSearch
    :topics: SearchHash/TheSequentialSearch
    :from_source: T
    :caption: Sequential Search of an Ordered List

    # Checks to see if item is in a list
    # retruns true or false
    # using ordered sequential search
    def orderedSequentialSearch(alist, item):
        pos = 0
        found = False
        stop = False
        while pos < len(alist) and not found and not stop:
            if alist[pos] == item:
                found = True
            else:
                if alist[pos] > item:
                    stop = True
                else:
                    pos = pos+1

        return found

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))