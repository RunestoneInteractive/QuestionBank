.. activecode::  ch18ex16q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPWebData
    :subchapter: Exercises
    :topics: CSPWebData/Exercises
    :from_source: T
    :nocodelens:

    file = open("stocks.txt", "r")
    lines = file.readlines()
    for line in lines:
        values = line.split(",")
        date = values[0]
        if date[0] == "1":
            print(date + " had a high value of " + values[2])