.. activecode:: hashtable1_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Using a Dictionary
    :optional:

    #shows how hash tables can be used in python
    def main():
        spnumbers = {"one":"uno","two":"dos"}

        spnumbers["four"]="cuatro"
        spnumbers["three"]="tres"

        print("one is", end=" ")
        print(spnumbers["one"])

        print(len(spnumbers))
    main()