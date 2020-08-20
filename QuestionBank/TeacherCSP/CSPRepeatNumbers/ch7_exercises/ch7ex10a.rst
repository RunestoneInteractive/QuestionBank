.. activecode::  ch7ex10a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    numbers = range(1, 11)
    for number in numbers:
            numString = str(number)
            square = str(number * number)
            print(numString + " * " + numString + " = " + square)