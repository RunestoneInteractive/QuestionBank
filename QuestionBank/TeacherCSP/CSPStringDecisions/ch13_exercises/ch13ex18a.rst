.. activecode::  ch13ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    def gradeAverage(aList):
        sum = 0
        for x in aList:
            sum = sum + x
        avg = sum / len(aList)
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
           grade = "F"
        return grade

    print(gradeAverage([80,90,90,80,100]))