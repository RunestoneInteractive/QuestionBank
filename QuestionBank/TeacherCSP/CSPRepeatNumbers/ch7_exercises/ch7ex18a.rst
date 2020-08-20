.. activecode::  ch7ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def aFunc(start, stop):
            sum = 0
            product = 1
            numbers = range(start, stop + 1)
            for number in numbers:
                    sum = sum + number
                    product = product * number
            average = (sum + product) / 2
            return average
    print(aFunc(1, 10))