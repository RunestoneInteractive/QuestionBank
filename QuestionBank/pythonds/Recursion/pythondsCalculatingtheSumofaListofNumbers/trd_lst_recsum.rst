.. activecode:: trd_lst_recsum
    :author: Majid Rouhani
    :difficulty: 0.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: pythondsCalculatingtheSumofaListofNumbers
    :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
    :from_source: F
    :caption: Recursive Summation - Correct the code so that the recursive function returns the sum of the values in the list

    def listsum(numList):
       if len(numList) == 1:
            return numList[0]
       else:
            return numList[0] + listsum(...)

    print(listsum([1,3,5,7,9]))