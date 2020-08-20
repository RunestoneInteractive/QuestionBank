.. activecode::  ch17ex13q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPStringPieces
     :subchapter: ch17_exercises
     :topics: CSPStringPieces/ch17_exercises
     :from_source: T
     :nocodelens:

     input = "Jay,shoes"
     pieces = input.split(",")
     name = pieces[0]
     item = pieces[1]
     print("One day " + name + " went shopping.")
     print("He wanted to buy " + item + ".")
     print("But, he didn't like any.")
     print("So, " + name + " went home.")