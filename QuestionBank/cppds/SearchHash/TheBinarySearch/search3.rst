.. codelens:: search3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheBinarySearch
    :topics: SearchHash/TheBinarySearch
    :from_source: T
    :caption: Binary Search of an Ordered List

    # Checks to see if item is in a list
    # retruns true or false
    # using binary Search
    def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False

        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return found

    def main():

        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        print(binarySearch(testlist, 3))
        print(binarySearch(testlist, 13))

    main()