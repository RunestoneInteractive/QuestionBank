.. activecode::  ch16ex11q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPIntroData
     :subchapter: Exercises
     :topics: CSPIntroData/Exercises
     :from_source: T
     :nocodelens:

     numbers = [0,1,2,3,4,5,6,7,8,9,10]
     evenList = []
     for index in range(0,len(numbers),2):
         evenList = evenList + [numbers[index]]
     print(evenList)