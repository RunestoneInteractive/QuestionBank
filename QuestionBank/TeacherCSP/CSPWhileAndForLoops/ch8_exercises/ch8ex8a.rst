.. activecode::  ch8ex8a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def sumFunc(start, stop):
        sum = 0
        num = start
        while num <= stop:
            sum = sum + num
            num = num + 1
        return sum
    print(sumFunc(1,10))