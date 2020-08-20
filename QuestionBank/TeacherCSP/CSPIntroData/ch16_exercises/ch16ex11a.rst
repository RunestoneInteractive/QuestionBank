.. activecode::  ch16ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def getEvenIndicesList(numbers):
        evenList = []
        for index in range(0,len(numbers),2):
            evenList = evenList + [numbers[index]]
        return(evenList)

    print(getEvenIndicesList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))