.. activecode:: active3_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Summation Without Iteration Python
    :optional:

    """ Performs same function as listing one, and also list the time it takes to perform
    the function, and it performs better with larger inputs or (n) """

    def sumOfN3(n):
        return (n*(n+1))//2

    def main():
        print(sumOfN3(10))
    main()