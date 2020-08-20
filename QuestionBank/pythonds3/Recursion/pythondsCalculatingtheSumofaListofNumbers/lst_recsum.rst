.. activecode:: lst_recsum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: pythondsCalculatingtheSumofaListofNumbers
    :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
    :from_source: T
    :caption: Recursive Summation

    def list_sum(num_list):
       if len(num_list) == 1:
            return num_list[0]
       else:
            return num_list[0] + list_sum(num_list[1:])

    print(list_sum([1, 3, 5, 7, 9]))