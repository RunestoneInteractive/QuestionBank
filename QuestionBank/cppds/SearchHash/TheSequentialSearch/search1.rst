.. codelens:: search1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheSequentialSearch
    :topics: SearchHash/TheSequentialSearch
    :from_source: T
    :caption: Sequential Search of an Unordered List

    # Checks to see if item is in a list
    # retruns true or false
    # using sequential search
    def sequentialSearch(alist, item):
        pos = 0
        found = False

        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1

        return found

    def main():
        testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        print(sequentialSearch(testlist, 3))
        print(sequentialSearch(testlist, 13))
    main()