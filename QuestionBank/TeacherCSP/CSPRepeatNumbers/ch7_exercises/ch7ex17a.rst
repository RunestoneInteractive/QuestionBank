.. activecode::  ch7ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def calculateProduct(lastNum):
        total = 1
        numList = range(2, lastNum + 1, 2)
        for num in numList:
            total = total * num
        return total

    print(calculateProduct(8))