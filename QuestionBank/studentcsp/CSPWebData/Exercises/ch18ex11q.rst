.. activecode::  ch18ex11q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPWebData
     :subchapter: Exercises
     :topics: CSPWebData/Exercises
     :from_source: T
     :nocodelens:

     inFile = open("uspoll.txt","r")
     line = inFile.readline()
     while line:
         values = line.split(":")
         pollution = float(values[2])
         if (pollution < 5):
             print('City: ', values[0])
             print("Pollution values:",values[1],values[2])
         line = inFile.readline()

     inFile.close()