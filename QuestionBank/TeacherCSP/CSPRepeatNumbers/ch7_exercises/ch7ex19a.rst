.. activecode::  ch7ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def getAverage(numList):
        sum = 0
        for num in numList:
            sum = sum + num
        return sum / len(numList)

    numberList = [90, 80, 75, 90, 83]
    print(getAverage(numberList))