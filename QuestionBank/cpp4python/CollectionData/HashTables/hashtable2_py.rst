.. activecode:: hashtable2_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: HashTables
    :topics: CollectionData/HashTables
    :from_source: T
    :caption: Iterating a Dictionary

    """Python equivalent
    of the C++ code """
    def main():
        spnumbers = {"one":"uno","two":"dos","three":"tres","four":"cuatro","five":"cinco" }

        for key in spnumbers:
            print(key, end=":")
            print(spnumbers[key])

    main()