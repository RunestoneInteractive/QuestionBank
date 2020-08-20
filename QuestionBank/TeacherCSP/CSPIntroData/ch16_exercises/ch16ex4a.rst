.. activecode::  ch16ex4a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    def nameProcedure(name):
        start = "My name is "
        combined = start + (name * 2)
        print(combined)
        print(len(combined))


    nameProcedure("John")