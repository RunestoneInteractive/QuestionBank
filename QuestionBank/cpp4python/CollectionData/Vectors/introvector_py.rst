.. activecode:: introvector_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Vectors
    :topics: CollectionData/Vectors
    :from_source: T
    :caption: Using a Python list

    """Uses a list to square every
    number from 0 to 49 """
    def main():
        intlist=[]
        for i in range(50):
            intlist.append(i*i)
            print(intlist[i])

    main()