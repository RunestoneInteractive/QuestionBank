.. activecode::  ch18ex4a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # loop through the lines
    for line in lines:
        if line[0] == "A" or line[0] == "B":
            print(line)