.. activecode:: introstring_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Python strings
    :optional:

    #shows basic string usage in Python
    def main():
        mystring1 = "Hello"
        mystring2 = "World!"

        mystring3 = mystring1 + " " + mystring2
        print(mystring3)

        print(mystring2, end=" ")
        print("begins at", end=" ")
        print(str(mystring3.find(mystring2)))

    main()