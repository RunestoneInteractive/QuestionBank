.. activecode:: iti
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: ThewhileStatement
    :topics: MoreAboutIteration/ThewhileStatement
    :from_source: None

    def sumTo(aBound):
        """ Return the sum of 1+2+3+...+aBound """

        theSum  = 0
        aNumber = 1
        while aNumber <= aBound:
            theSum = theSum + aNumber
            aNumber = aNumber + 1
        return theSum

    print(sumTo(4))

    print(sumTo(1000))