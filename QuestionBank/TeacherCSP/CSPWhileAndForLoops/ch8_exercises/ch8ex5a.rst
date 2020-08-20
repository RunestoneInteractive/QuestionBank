.. activecode::  ch8ex5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    output = ""
    x = -5
    while x < 0:
        output = output + str(x) + " "
        x = x + 1
    print(output)