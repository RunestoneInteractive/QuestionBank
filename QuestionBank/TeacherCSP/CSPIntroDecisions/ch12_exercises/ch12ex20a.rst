.. activecode::  ch12ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens:

    x = 3
    if x % 3 == 0:
        print("Fizz")
    if x % 5 == 0:
        print("Buzz")
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")