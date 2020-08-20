.. activecode::  ch8ex10a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    x = 1

    while x < 4:
        for y in range(1,11):
            print(str(x) + " * " + str(y) + " = " + str(x*y))
        x += 1