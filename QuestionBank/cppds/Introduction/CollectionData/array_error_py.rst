.. activecode:: array_error_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Iterating a list in Python
    :optional:

    #outputs the result of trying to access a value outside of an array
    def main():
        mylist = [2,4,6,8]
        print(mylist)
        for i in range(5):
            print(mylist[i])
            print("id: "+str(id(mylist[i])))

    main()