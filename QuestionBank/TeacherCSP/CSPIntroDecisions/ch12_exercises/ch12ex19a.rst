.. activecode::  ch12ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens:

    def getGrade(x):
        if x >= 90:
           return "A"
        if x >= 80 and x < 90:
           return "B"
        if x >= 70 and x < 80:
           return "C"
        if x >= 60 and x < 70:
           return "D"
        if x < 60:
           return "E"

    print(getGrade(95))
    print(getGrade(90))
    print(getGrade(85))
    print(getGrade(80))
    print(getGrade(75))
    print(getGrade(70))
    print(getGrade(65))
    print(getGrade(60))
    print(getGrade(55))
    print(getGrade(50))
    print(getGrade(0))