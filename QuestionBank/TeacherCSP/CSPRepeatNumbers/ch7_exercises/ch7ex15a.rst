.. activecode::  ch7ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def sumOdd(lastNumber):
        sum = 0
        numList = range(1,lastNumber+1,2)
        for num in numList:
            sum = sum + num
        return sum

    print(sumOdd(13))