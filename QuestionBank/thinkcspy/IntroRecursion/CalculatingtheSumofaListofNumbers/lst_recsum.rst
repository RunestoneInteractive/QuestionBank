.. activecode:: lst_recsum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: CalculatingtheSumofaListofNumbers
    :topics: IntroRecursion/CalculatingtheSumofaListofNumbers
    :from_source: T
    :caption: Recursive Summation

    def listsum(numList):
       if len(numList) == 1:
            return numList[0]
       else:
            return numList[0] + listsum(numList[1:])

    print(listsum([1,3,5,7,9]))