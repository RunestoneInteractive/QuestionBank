.. activecode:: ec2py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Python
    :optional:

    import time

    """ Performs same function as listing one, and also list the time it takes to perform
    the function """

    def sumOfN2(n):
        start = time.time()

        theSum = 0
        for i in range(1,n+1):
            theSum = theSum + i

        end = time.time()
        elapsed = end-start
        print("Sum is", theSum, "required", elapsed, "seconds")

        return elapsed

    def main():
        for i in range(5):
            sumOfN2(10000)
    main()