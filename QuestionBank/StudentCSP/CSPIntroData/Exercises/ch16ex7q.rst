.. activecode::  ch16ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPIntroData
     :subchapter: Exercises
     :topics: CSPIntroData/Exercises
     :from_source: T
     :nocodelens:

     source = ["This","is","a","list"]
     soFar = []
     for index in range(0,len(source)):
     soFar = [source[index]] + soFar
     print(soFar)