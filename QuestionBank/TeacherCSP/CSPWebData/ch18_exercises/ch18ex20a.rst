.. activecode::  ch18ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def firstDayChange(file):
        file = open(file, "r")
        lines = file.readlines()
        maxChange = 0
        for line in lines:
            values = line.split(",")
            dateParts = values[0].split("-")
            day = int(dateParts[0])

            if day == 1:
                high = float(values[2])
                low = float(values[3])
                change = high - low

                if change > maxChange:
                    maxChange = change
                    date = values[0]
        print(date + " had the max change of " + str(maxChange))

    firstDayChange("stocks.txt")