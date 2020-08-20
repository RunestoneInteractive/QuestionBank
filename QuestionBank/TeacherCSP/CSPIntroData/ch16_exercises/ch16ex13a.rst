.. activecode::  ch16ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens

    def countdown(start):
        for index in range(start, -1, -1):
            print(index)

    countdown(10)