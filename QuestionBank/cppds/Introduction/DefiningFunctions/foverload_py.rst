.. activecode:: foverload_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: DefiningFunctions
    :topics: Introduction/DefiningFunctions
    :from_source: T
    :caption: Function Overloading in Python
    :optional:

    #showcases function overloading in Python
    def myfunct(n, m=None):
        if m is None:
            print("1 parameter: " + str(n))
        else:
            print("2 parameters: " + str(n), end="")
            print(" and ", str(m))

    def main():
        myfunct(4);
        myfunct(5, 6);
        myfunct(100);

    main()