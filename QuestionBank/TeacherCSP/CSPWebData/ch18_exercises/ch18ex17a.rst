.. activecode::  ch18ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def pointChange(file, year):
        file = open(file, "r")
        lines = file.readlines()
        max = 0
        min = 1000000
        for line in lines:
            values = line.split(",")
            dateParts = values[0].split("-")
            if dateParts[2] == year:
                high = float(values[2])
                low = float(values[3])
                if high > max:
                    max = high
                if low < min:
                    min = low
        print(max - min)

    pointChange("stocks.txt", "89")