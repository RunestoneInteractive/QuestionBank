.. activecode:: binary_search_python_array
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheBinarySearch
    :topics: SearchHash/TheBinarySearch
    :from_source: T
    :caption: Optimized Binary Search
    :optional:

    '''Checks to see if item is in a list
    retruns true or false (1 or 0)
    using binary Search and
    uses start and end indices'''

    def binarySearch(array, item, start, end):

        if end == start:
            return False
        if end >= start:
            mid = start + (end - start) // 2
            if array[mid] == item:
                return True
            if array[mid] > item:
                return binarySearch(array, item, start, mid - 1)
            else:
                return binarySearch(array, item, mid + 1, end)

        return False

    def main():
        array = [0, 1, 2, 8, 13, 17, 19, 32, 42]

        a = binarySearch(array, 17, 0 , len(array))
        print("answer is ", a)
        b = binarySearch(array, 99, 0, len(array))
        print("answer is", b)
    main()