.. activecode:: address_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Memory identifier in Python
    :optional:

    #because python is an interpreted language, variables stored at a virtual memory address.
    def main():
        varN = 101;
        print(varN)
        print(id(varN))

    main()