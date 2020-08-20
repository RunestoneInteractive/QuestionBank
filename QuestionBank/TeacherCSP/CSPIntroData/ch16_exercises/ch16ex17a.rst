.. activecode::  ch16ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def sumPos(theList):
        sum = 0
        for item in theList:
            if item >= 0:
                sum = sum + item
        return sum

    print(sumPos([-3, 2, -8, 5, -20, -33, 15]))