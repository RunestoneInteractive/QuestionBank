.. activecode::  ch18ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    file = open("stocks.txt", "r")
    lines = file.readlines()
    maxGain = 0
    for line in lines:
        values = line.split(",")
        open = float(values[1])
        close = float(values[4])
        perChange = ((close - open) / open) * 100
        if perChange > maxGain:
            maxGain = perChange
            date = values[0]
    print(date)