.. activecode::  ch18ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def monthAvg(file, month):
        file = open(file, "r")
        lines = file.readlines()
        count = 0
        sum = 0
        for line in lines:
            values = line.split(",")
            dateParts = values[0].split("-")
            if dateParts[1] == month:
                close = float(values[4])
                sum = sum + close
                count += 1
        return sum / count

    print(monthAvg)