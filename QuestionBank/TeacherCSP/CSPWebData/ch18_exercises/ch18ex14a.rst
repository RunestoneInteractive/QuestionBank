.. activecode::  ch18ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def pointGain(file):
        lines = file.readlines()
        for line in lines:
            values = line.split(",")
            open = float(values[1])
            close = float(values[4])
            if (close - open) > 300:
                print(values[0])
    file = open("stocks.txt", "r")
    pointGain(file)