.. activecode:: ch07_summation
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Theforlooprevisited
    :topics: MoreAboutIteration/Theforlooprevisited
    :from_source: T

    def sumTo(aBound):
        theSum = 0
        for aNumber in range(1, aBound + 1):
            theSum = theSum + aNumber

        return theSum

    print(sumTo(4))

    print(sumTo(1000))