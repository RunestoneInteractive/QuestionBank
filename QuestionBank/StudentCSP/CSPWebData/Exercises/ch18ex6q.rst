.. activecode::  ch18ex6q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPWebData
    :subchapter: Exercises
    :topics: CSPWebData/Exercises
    :from_source: T
    :nocodelens:

    # read all the lines
    inFile = open("uspoll.txt", r)
    lines = inFile.readline
    inFile.close()

    # loop through the lines
    for line in lines:

        # split at :
        values = line.split(" ")

        # get the min PM 2.5 pollution and the city
        num = str(values[2])
        city = values[0]

        # check if even
        if num % 2 == 0:

        # print the values
        print("Even min PM 2.5 ", num ," in ", city)