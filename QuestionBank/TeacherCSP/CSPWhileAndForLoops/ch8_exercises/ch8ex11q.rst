.. activecode::  ch8ex11q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPWhileAndForLoops
     :subchapter: ch8_exercises
     :topics: CSPWhileAndForLoops/ch8_exercises
     :from_source: T
     :nocodelens:

     product = 1  # Start out with nothing
     numbers = range(1,11)
     for number in numbers:
         product = product * number
     print(product)