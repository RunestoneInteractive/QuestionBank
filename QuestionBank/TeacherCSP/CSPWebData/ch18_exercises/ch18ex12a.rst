.. activecode::  ch18ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens

    def printPollution(inFile,cityName):

        lines = inFile.readlines()

        for line in lines:
            values = line.split(":")
            city = values[0]
            if (city.find(cityName) == 0):
                print('City: ', city)
                print("Pollution values:",values[1],values[2])

    inFile = open("uspoll.txt","r")
    printPollution(inFile, "Albany, GA")
    inFile.close()