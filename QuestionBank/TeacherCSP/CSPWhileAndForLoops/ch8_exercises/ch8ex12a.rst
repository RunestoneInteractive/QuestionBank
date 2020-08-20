.. activecode::  ch8ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    sum = 0
    x = 1
    while x < 11:
        sum = sum + x
        x = x + 1
    average = sum / x
    print(average)