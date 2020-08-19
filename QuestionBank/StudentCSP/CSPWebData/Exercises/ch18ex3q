.. activecode::  ch18ex3q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPWebData
     :subchapter: Exercises
     :topics: CSPWebData/Exercises
     :from_source: T
     :nocodelens:

     inFile = open("uspoll.txt","r"
     lines = inFile.readlines()
     inFile.Close()

     maxCity = ''
     max25 =   # initialize max25
     for line  lines:
         values = line.split(":")
         new25 = float(values[2]) # get the current value
         if new25 > max25
             maxCity = values[0]
             max25 = new25 # save the new maximum
     print("Largest PM 2.5 value is ",max25," in ",maxCity)