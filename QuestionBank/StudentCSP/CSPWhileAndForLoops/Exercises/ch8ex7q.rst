.. activecode::  ch8ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPWhileAndForLoops
     :subchapter: Exercises
     :topics: CSPWhileAndForLoops/Exercises
     :from_source: T
     :nocodelens:

     target = 6
         guess = 2
     guessSquared = guess * guess
     while abs(target-guessSquared) > 0.01:
         closer = target / guess
     guess = (guess + closer) / 2.0
             guessSquared = guess * guess
         print("Square root of", target,"is", guess)