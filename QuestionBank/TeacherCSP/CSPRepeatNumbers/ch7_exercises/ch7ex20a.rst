.. activecode::  ch7ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def aFunc(stop):
            evens = range(0, stop + 1, 2)
            odds = range( 1, stop + 1, 2)
            product = 1
            sum = 0
            for n in evens:
                    product = product * n
            for n in odds:
                    sum = sum + n
            difference = product - sum
            average = (product + sum) / 2
            return difference/ average
    print(aFunc(10))