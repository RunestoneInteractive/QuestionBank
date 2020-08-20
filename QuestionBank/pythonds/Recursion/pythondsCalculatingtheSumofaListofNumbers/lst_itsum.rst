.. activecode:: lst_itsum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: pythondsCalculatingtheSumofaListofNumbers
    :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
    :from_source: T
    :caption: Iterative Summation

    def listsum(numList):
        theSum = 0
        for i in numList:
            theSum = theSum + i
        return theSum

    print(listsum([1,3,5,7,9]))