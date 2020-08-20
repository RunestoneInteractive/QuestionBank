.. activecode::  ch18ex8a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def vowelFinder(file):
        inFile = open(file,"r")
        line = inFile.readline()
        while line:
            values = line.split(":")
            city = values[0]
            if (city.find("A") == 0 or city.find("E") == 0):
                print('City: ', city, "Pollution values:",values[1],values[2])
            if (city.find("I") == 0 or city.find("O") == 0):
                print('City: ', city, "Pollution values:",values[1],values[2])
            if (city.find("U") == 0):
                print('City: ', city, "Pollution values:",values[1],values[2])

            line = inFile.readline()

        inFile.close()

    vowelFinder("uspoll.txt")