.. activecode::  ch18ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def findPM25LessThan(inFile, amount):
        line = inFile.readline()
        while line:
            values = line.split(":")
            pollution = float(values[2])
            if (pollution < amount):
                print('City: ', values[0])
                print("Pollution values:",values[1],values[2])
            line = inFile.readline()

    inFile = open("uspoll.txt","r")
    findPM25LessThan(inFile,5)
    inFile.close()