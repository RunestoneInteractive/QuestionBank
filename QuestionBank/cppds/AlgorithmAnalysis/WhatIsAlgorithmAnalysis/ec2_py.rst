.. activecode:: ec2_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Another Summation of the First n Integers in python
    :optional:

    #Performs same function as listing 1, but is less descriptive
    #This is not good practice

    def foo(tom):
        fred = 0
        for bill in range(1,tom+1):
            barney = bill
            fred = fred + barney

        return fred

    def main():
        print(foo(10))
    main()