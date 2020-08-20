.. activecode::  ch8ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def calculateSum(lastNum):
        sum = 0
        num = 0
        while (num <= lastNum):
            sum = sum + num
            num = num + 2
        return sum

    print(calculateSum(10))