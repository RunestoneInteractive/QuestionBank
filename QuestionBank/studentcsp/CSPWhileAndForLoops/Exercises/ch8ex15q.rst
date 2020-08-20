.. activecode::  ch8ex15q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPWhileAndForLoops
     :subchapter: Exercises
     :topics: CSPWhileAndForLoops/Exercises
     :from_source: T
     :nocodelens:

     sum = 0
     count = 0
     message = "Enter an integer or a negative number to stop"
     value = input(message)
     while int(value) > 0:
         print("You entered " + value)
         sum = sum + int(value)
         count = count + 1
         value = input(message)
     print("The sum is: " + str(sum) +
           " the average is: " + str(sum / count))