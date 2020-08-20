.. activecode:: lst_itsum
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: IntroRecursion
    :subchapter: CalculatingtheSumofaListofNumbers
    :topics: IntroRecursion/CalculatingtheSumofaListofNumbers
    :from_source: None
    :caption: Iterative Summation

    def listsum(numList):
        theSum = 0
        for i in numList:
            theSum = theSum + i
        return theSum

    print(listsum([1,3,5,7,9]))