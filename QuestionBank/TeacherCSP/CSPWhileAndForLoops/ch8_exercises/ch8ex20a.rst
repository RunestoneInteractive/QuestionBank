.. activecode::  ch8ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def triangleDraw(n):
        x = 1
        while x <= n:
            print("*" * x)
            x += 1

    triangleDraw(6)