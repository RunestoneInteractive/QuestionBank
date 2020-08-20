.. activecode:: array_error_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Iterating a list in Python

    """Demonstrates how python protects from
    iterating past the end of a list,
     and shows the use of Id as the location in memory"""
    def main():
        mylist = [2,4,6,8]
        print(mylist)
        for i in range(5):
            print(mylist[i])
            print("id: "+str(id(mylist[i])))

    main()