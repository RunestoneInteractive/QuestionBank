.. activecode::  ch18ex2a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    total25 = 0
    count = 1.0
    for line in lines:
        values = line.split(":")
        new25 = float(values[2])
        city = values[0]
        if (city.find("A") == 0):
            total25 = total25 + new25
            count = count + 1

    print("Average PM 2.5 value for cities that start with 'A' is ", total25/count)