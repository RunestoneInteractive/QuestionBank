.. codelens:: search2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: SortSearch
    :subchapter: TheSequentialSearch
    :topics: SortSearch/TheSequentialSearch
    :from_source: T
    :caption: Sequential Search of an Ordered List

    def ordered_sequential_search(a_list, item):
        pos = 0
        while pos < len(a_list):
            if a_list[pos] == item:
                return True
            else:
                if a_list[pos] > item:
                    return False
                else:
                    pos = pos + 1

        return False


    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(ordered_sequential_search(test_list, 3))
    print(ordered_sequential_search(test_list, 13))