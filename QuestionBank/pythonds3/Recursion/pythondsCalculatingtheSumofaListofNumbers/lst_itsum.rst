.. activecode:: lst_itsum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: pythondsCalculatingtheSumofaListofNumbers
    :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
    :from_source: T
    :caption: Iterative Summation

    def list_sum(num_list):
        the_sum = 0
        for i in num_list:
            the_sum = the_sum + i
        return the_sum

    print(list_sum([1, 3, 5, 7, 9]))