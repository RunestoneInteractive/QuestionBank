.. activecode:: charpy
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Python strings
    :optional:

    #outputs the boolean results to show how strings and chars differ in C++
    def main():

        strvar = "b"
        charvar = 'b'

        print('b' == charvar)
        print("b" == strvar)
        print('a' == "a")

    main()