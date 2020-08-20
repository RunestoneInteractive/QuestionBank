.. activecode::  ch17ex11q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPStringPieces
     :subchapter: ch17_exercises
     :topics: CSPStringPieces/ch17_exercises
     :from_source: T
     :nocodelens:

     input = "Elvis, alien, blue"
     pieces = input.split(",")
     name = pieces[0]
     thing = pieces[1]
     color = pieces[2]
     headline = name + " was abducted by a " + color + " " + thing + "."
     print(headline)