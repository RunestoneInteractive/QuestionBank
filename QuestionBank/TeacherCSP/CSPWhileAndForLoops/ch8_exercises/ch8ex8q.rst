.. activecode::  ch8ex8q
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
        for num in range(start, stop + 1):
            sum = sum + num
        return sum

    print(sumFunc(1,10))