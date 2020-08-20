.. activecode::  ch17ex13q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPStringPieces
     :subchapter: Exercises
     :topics: CSPStringPieces/Exercises
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