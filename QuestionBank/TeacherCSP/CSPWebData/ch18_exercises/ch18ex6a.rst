.. activecode::  ch18ex6a
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

        # split at :
        values = line.split(":")

        # get the min PM 2.5 pollution and the city
        num = float(values[2])
        city = values[0]

        # check if even
        if num % 2 == 0:

            # print the values
            print("Even min PM 2.5 ", num ," in ", city)