.. activecode::  ch7ex7a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def calculateProduct(numbers):
        product = 1  # Start out with 1
        for number in numbers:
            product = product * number
        return(product)

    numbers = [1,2,3,4,5]
    print(calculateProduct(numbers))