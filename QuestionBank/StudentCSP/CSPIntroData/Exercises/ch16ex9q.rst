.. activecode::  ch16ex9q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPIntroData
     :subchapter: Exercises
     :topics: CSPIntroData/Exercises
     :from_source: T
     :nocodelens:

     # setup the source list
     source = ["This","is" "a","list"]

     # Set the accumulator to the empty list
     soFar = [

     # Loop through all the items in the source list
     for index in range(0,len(source))

         # Add the current item in the source and print the current items in soFar
         soFar = [source[index]] + sofar
         print(soFar)