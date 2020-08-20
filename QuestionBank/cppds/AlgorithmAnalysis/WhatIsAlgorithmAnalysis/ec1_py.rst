.. activecode:: ec1_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Python
    :optional:

    # adds the sum of (n + n-1 + n-2 ...)
    def sumOfN(n):
        theSum = 0
        for i in range(1,n+1):
            theSum = theSum + i

        return theSum

    def main():
        print(sumOfN(10)) # n is 10 (10 + 9 + 8 ...)
    main()