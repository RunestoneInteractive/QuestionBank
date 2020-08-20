.. activecode::  ch16ex6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def gradeAverage(aList):
        sum = 0
        for num in aList:
            sum = sum + num
        average =  sum / len(aList)
        return average

    aList = [99, 100, 74, 63, 100, 100]
    print(gradeAverage(aList))