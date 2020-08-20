.. activecode:: array_werror_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Write error in Python

    """Demonstrates how python protects from
    iterating past the end of a list
    and changing any other data"""
    def main():
        mylist = [2, 4]
        otherdata = [777, 777]
        for i in range(4):
            print(mylist[i])
            print("id: "+str(id(mylist[i])))

        for j in range(2):
              print(otherdata[i])
              print("id: "+str(id(otherdata[i])))

    main()