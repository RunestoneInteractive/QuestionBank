.. activecode::  ch13ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    for x in range (1,21):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)