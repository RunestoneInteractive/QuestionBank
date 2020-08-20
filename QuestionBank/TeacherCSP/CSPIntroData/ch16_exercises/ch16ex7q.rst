.. activecode::  ch16ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPIntroData
     :subchapter: ch16_exercises
     :topics: CSPIntroData/ch16_exercises
     :from_source: T
     :nocodelens:

     source = ["This","is","a","list"]
     soFar = []
     for index in range(0,len(source)):
     soFar = [source[index]] + soFar
     print(soFar)