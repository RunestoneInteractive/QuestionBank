.. activecode::  ch7ex4a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    product = 1
    numbers = range(5,26,5)
    for number in numbers:
            product = product * number
    print(product)