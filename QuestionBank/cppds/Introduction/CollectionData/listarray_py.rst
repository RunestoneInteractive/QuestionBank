.. activecode:: listarray_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Iterating a list in Python
    :optional:

    #showcases an iteration through an array in Python
    def main():
        mylist = [2, 4, 6, 8]
        for i in range(4):
            print(mylist[i])

    main()