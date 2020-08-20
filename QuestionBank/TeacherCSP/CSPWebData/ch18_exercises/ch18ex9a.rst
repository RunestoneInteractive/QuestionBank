.. activecode::  ch18ex9a
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPWebData
     :subchapter: ch18_exercises
     :topics: CSPWebData/ch18_exercises
     :from_source: T
     :nocodelens:

     def findPM10GreaterThan(inFile, amount):
         line = inFile.readline()
         while line:
             values = line.split(":")
             pollution = float(values[1])
             if (pollution > amount):
                 print('City: ', values[0])
                 print("Pollution values:",values[1],values[2])
             line = inFile.readline()

     inFile = open("uspoll.txt","r")
     findPM10GreaterThan(inFile,25)
     inFile.close()