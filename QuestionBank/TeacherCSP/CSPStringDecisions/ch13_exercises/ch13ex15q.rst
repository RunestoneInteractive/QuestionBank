.. activecode::  ch13ex15q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPStringDecisions
     :subchapter: ch13_exercises
     :topics: CSPStringDecisions/ch13_exercises
     :from_source: T
     :nocodelens:

     x = .25
     if x <= .25:
         print("x is in the first quartile - x <= .25")
     if x <= .5 and x > .25:
         print("x is in the second quartile - .25 < x <= .5")
     if x <= .75 and x > .5:
         print("x is in the third quartile - .5 < x <= .75")
     if x > .75:
         print("x is in the fourth quartile - .75 < x <= 1")