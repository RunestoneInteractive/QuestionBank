.. activecode:: listarray_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Iterating a list in Python

    """Demonstrates how python protects from
    iterating past the end of a list"""

    def main():
        mylist = [2, 4, 6, 8]
        for i in range(8):
            print(mylist[i])

    main()