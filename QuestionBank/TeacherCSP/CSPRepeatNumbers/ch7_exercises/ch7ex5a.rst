.. activecode::  ch7ex5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    product = 1  # Start out with nothing
    numbers = [1,2,3,4,5]
    for number in numbers:
        product = product * number
    print(product)