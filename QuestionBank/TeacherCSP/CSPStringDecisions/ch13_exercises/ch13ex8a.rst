.. activecode::  ch13ex8a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    numbers = [-1,0,1]
    for x in numbers:
        if x > 0:
            print("positive")
        elif x < 0:
            print("negative")
        else:
            print("neither")