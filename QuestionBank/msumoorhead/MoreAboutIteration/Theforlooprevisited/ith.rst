.. activecode:: ith
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: Theforlooprevisited
    :topics: MoreAboutIteration/Theforlooprevisited
    :from_source: None

    def sumTo(aBound):
        theSum = 0
        for aNumber in range(1, aBound + 1):
            theSum = theSum + aNumber

        return theSum

    print(sumTo(4))

    print(sumTo(1000))