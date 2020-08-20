.. activecode::  ch7ex3a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def sumNums(numList):
        sum = 0
        for number in numList:
            sum = sum + number
        return sum

    aList = [1,2,3,4,5]
    print(sumNums(aList))