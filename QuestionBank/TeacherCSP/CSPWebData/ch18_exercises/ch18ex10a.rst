.. activecode::  ch18ex10a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def averagePM(file):
        # read all the lines
        inFile = open(file,"r")
        lines = inFile.readlines()
        inFile.close()
        sum = 0
        count = 0
        # loop through the lines
        for line in lines:
            values = line.split(":")
            if line[0] == "L":
                pm = float(values[2])
                sum = sum + pm
                count += 1
        return sum / count

    print(averagePM("uspoll.txt"))