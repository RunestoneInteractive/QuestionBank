.. activecode::  file_ex_Juneq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:

    file = open("stocks.txt", "r")
    lines = file.readlines()
    for line in lines:
        values = line.split(",")
        date = values[0]
        if date[0] == "1":
            print(date + " had a high value of " + values[2])