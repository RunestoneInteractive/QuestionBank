.. activecode::  ch16ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def aProcedure(num):
        newList = []
        sum = 0
        for i in range(1, num + 1, 4):
            newList = newList + [i]
            sum = sum + i
        print(newList)
        print(sum)
    aProcedure(20)