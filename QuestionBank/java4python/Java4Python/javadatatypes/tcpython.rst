.. activecode:: tcpython
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: javadatatypes
    :topics: Java4Python/javadatatypes
    :from_source: T
    :language: python

    def main():
        fahr = int(input("Enter the temperature in F: "))
        cel = (fahr - 32) * 5.0/9.0
        print("the temperature in C is: ", cel)

    main()