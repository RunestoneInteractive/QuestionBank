.. activecode::  ch16ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def listAdder(aList):
        for x in range(len(aList)):
            aList[x] = aList[x] + 5
        return aList
    nums = [1,2,3]
    print(listAdder(nums))