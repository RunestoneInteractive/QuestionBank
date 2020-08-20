.. activecode:: introvector_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Using a Python list
    :optional:

    #Python doesn't have vectors, simply stating the limit is enough
    def main():
        intlist=[]
        for i in range(50):
            intlist.append(i*i)
            print(intlist[i])

    main()