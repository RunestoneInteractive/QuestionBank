.. activecode::  ch13ex5q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPStringDecisions
     :subchapter: ch13_exercises
     :topics: CSPStringDecisions/ch13_exercises
     :from_source: T
     :nocodelens:

     score = 80
     if score >= 90:
         grade = "A"
     if score >= 80:
         grade = "B"
     if score >= 70:
         grade = "C"
     if score >= 60:
         grade = "D"
     if score < 60:
        grade = "E"
     print(grade)