.. codelens:: search1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: SortSearch
    :subchapter: TheSequentialSearch
    :topics: SortSearch/TheSequentialSearch
    :from_source: T
    :caption: Sequential Search of an Unordered List

    def sequential_search(a_list, item):
        pos = 0

        while pos < len(a_list):
            if a_list[pos] == item:
                return True
            else:
                pos = pos + 1

        return False


    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list, 3))
    print(sequential_search(test_list, 13))