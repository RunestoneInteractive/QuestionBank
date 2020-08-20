.. activecode:: hashtable1_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: HashTables
    :topics: CollectionData/HashTables
    :from_source: T
    :caption: Using a Dictionary

    """Python equivalent
    of the C++ code """
    def main():
        spnumbers = {"one":"uno","two":"dos"}

        spnumbers["four"]="cuatro"
        spnumbers["three"]="tres"

        print("one is", end=" ")
        print(spnumbers["one"])

        print(len(spnumbers))
    main()