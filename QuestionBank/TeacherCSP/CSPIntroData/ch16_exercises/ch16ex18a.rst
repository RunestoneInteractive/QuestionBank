.. activecode::  ch16ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def aFunction(aList):
        posSum = 0
        negSum = 0
        for x in aList:
            if x >= 0:
                posSum = posSum + x
            else:
                negSum = negSum + x
        avg = (posSum + (negSum * -1))/2
        return avg

    nums = [-3,-1,2,4]
    print(aFunction(nums))