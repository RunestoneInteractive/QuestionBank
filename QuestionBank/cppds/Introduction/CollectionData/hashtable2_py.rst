.. activecode:: hashtable2_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Iterating a Dictionary
    :optional:

    #shows how to iterate through a hash table in python
    def main():
        spnumbers = {"one":"uno","two":"dos","three":"tres","four":"cuatro","five":"cinco" }

        for key in spnumbers:
            print(key, end=":")
            print(spnumbers[key])

    main()