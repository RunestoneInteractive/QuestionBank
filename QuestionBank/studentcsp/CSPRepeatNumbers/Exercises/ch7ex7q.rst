.. activecode::  ch7ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPRepeatNumbers
     :subchapter: Exercises
     :topics: CSPRepeatNumbers/Exercises
     :from_source: T
     :nocodelens:

     product = 1  # Start out with 1
     numbers = [1,2,3,4,5]
     for number in numbers:
         product = product * number
     print(product)