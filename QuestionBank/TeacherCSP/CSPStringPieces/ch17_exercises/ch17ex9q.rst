.. activecode::  ch17ex9q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPStringPieces
     :subchapter: ch17_exercises
     :topics: CSPStringPieces/ch17_exercises
     :from_source: T
     :nocodelens:

     namePart = "name: Anu Gao"
     posName = namePart.find("name:")
     if (posName > -1):
         name = namePart[posName+6:len(namePart)]
     else:
         name = "Unknown"
     print(name)