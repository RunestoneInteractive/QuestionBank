.. activecode:: active1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Summation of the First n Integers

    def sum_of_n(n):
        the_sum = 0
        for i in range(1, n + 1):
            the_sum = the_sum + i

        return the_sum


    print(sum_of_n(10))