.. activecode::  ch18ex16a
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
    for line in lines:
        values = line.split(",")
        date = values[0]
        dateParts = date.split("-")
        month = dateParts[1]
        if month == "Jun":
            print(date + "had a high value of " + values[2])