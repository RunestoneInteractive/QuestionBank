.. codelens:: search4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheBinarySearch
    :topics: SearchHash/TheBinarySearch
    :from_source: T
    :caption: A Binary Search--Recursive Version

    # Checks to see if item is in a list
    # retruns true or false
    # using binary Search recursively
    def binarySearch(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist)//2
            if alist[midpoint]==item:
              return True
            else:
              if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
              else:
                return binarySearch(alist[midpoint+1:],item)

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))