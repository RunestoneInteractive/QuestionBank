.. activecode:: func_7
    :author: DANIEL LEE
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
  
    Look at the code below and complete this sentence: "___ is a temporary 
    variable because ___."
 
    def maximum(y, x):

        max = max(y, x)

        return max
 		
    firstNum = input("Enter the first number:")

    secNum = input("Enter the second number:")

    maxResult = maximum(firstNum, secNum)

    print("The bigger number is... ", maxResult, "!")

    ~~~~