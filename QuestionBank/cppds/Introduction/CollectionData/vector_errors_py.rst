.. activecode:: vector_errors_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Python list out of bounds
    :optional:

    #shows errors when a vector goes out of bounds
    def main():
        intlist=[]
        for i in range(10):
            intlist.append(i)

        for i in range(11):
            print("intlist[" + str(i) + "]=" + str(intlist[i]))

    main()