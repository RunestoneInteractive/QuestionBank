.. activecode:: ProbSolv2017-18_Lab_02
    :author: Max Garagnani
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
 

    ~~~~
    # This program calculates the product of the first n negative integers

    n = int(input("Enter a positive integer: "))
    result = -1
    for i in range(-n,-1,1):
        result = result * i
        print(" Factoring in ", i)
    print("The product of the first", n, " negative integers is: ", result)