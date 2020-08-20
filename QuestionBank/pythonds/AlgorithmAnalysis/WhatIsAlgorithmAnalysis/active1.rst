.. activecode:: active1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Summation of the First n Integers

    def sumOfN(n):
       theSum = 0
       for i in range(1,n+1):
           theSum = theSum + i

       return theSum

    print(sumOfN(10))