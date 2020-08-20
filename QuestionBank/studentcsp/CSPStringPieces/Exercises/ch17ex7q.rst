.. activecode::  ch17ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPStringPieces
     :subchapter: Exercises
     :topics: CSPStringPieces/Exercises
     :from_source: T
     :nocodelens:

     input = "Roses,Violets,Sugar,Sue"
     pieces = input.split(",")
     flower1 = pieces[1]
     flower2 = pieces[2]
     spice = pieces[3]
     name = pieces[4]
     line1 = flower1 + " are red"
     line2 = flower2 + " are blue"
     line3 = spice + " is sweet"
     line4 = "And so it " + name
     print(line1)
     print(line2)
     print(line3)
     print(line4)