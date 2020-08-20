.. activecode:: active6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: AlgorithmAnalysis
    :subchapter: AnAnagramDetectionExample
    :topics: AlgorithmAnalysis/AnAnagramDetectionExample
    :from_source: T
    :caption: Sort and Compare

    def anagram_solution_2(s1, s2):
        a_list_1 = list(s1)
        a_list_2 = list(s2)

        a_list_1.sort()
        a_list_2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if a_list_1[pos] == a_list_2[pos]:
                pos = pos + 1
            else:
                matches = False

        return matches


    print(anagram_solution_2("apple", "pleap"))  # expected: True
    print(anagram_solution_2("abcd", "dcba"))  # expected: True
    print(anagram_solution_2("abcd", "dcda"))  # expected: False