.. activecode::  ch8ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    product = 1  # Start out with nothing
    number = 1
    while number < 11:
        product = product * number
        number = number + 1
    print(product)