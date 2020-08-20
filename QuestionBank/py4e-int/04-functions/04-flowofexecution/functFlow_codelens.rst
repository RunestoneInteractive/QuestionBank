.. codelens:: functFlow_codelens
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-flowofexecution
    :topics: 04-functions/04-flowofexecution
    :from_source: T
    :showoutput:

    def firstPrint():
        print("First")
        secondPrint()

    def secondPrint():
        print("Second")
        thirdPrint()

    def thirdPrint():
        print("Third")

    firstPrint()