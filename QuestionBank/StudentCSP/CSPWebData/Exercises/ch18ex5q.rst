.. activecode::  ch18ex5q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPWebData
     :subchapter: Exercises
     :topics: CSPWebData/Exercises
     :from_source: T
     :nocodelens:

     inFile = open("uspoll.txt","r")
     lines = inFile.readlines()
     inFile.close()

     minCity = ''
     min25 = 500
     for line in lines:
     values = line.split(":")
     new25 = float(values[2]) # set the value for new25 to be the current PM 2.5 value
     if new25 < min25:
     minCity = values[0] # Save the minimum city and state
     min25 = new25 # save the minimum PM 2.5 value
     print("Smallest PM 2.5 ",min25," in ",minCity)