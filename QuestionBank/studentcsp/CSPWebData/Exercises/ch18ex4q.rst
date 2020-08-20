.. activecode::  ch18ex4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPWebData
    :subchapter: Exercises
    :topics: CSPWebData/Exercises
    :from_source: T
    :nocodelens:

    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # loop through the lines
    for line in lines:
        if line[0] == "A":
            print(line)