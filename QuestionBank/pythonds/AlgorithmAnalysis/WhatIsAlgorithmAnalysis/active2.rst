.. activecode:: active2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Another Summation of the First n Integers

    def foo(tom):
        fred = 0
        for bill in range(1,tom+1):
           barney = bill
           fred = fred + barney

        return fred

    print(foo(10))