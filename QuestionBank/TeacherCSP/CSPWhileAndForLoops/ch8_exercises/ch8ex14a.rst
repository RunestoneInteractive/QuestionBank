.. activecode::  ch8ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    number = 0
    while number < 10:
        while number % 2 == 0:
            print("Even")
            number += 1
        while number % 2 != 0:
            print("Odd")
            number += 1