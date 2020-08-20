.. activecode::  ch18ex13q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def biggestLoss(file):
        maxLoss = 0
        lines = file.readlines()
        for # in lines:
            values = line.split(#)
            open = float(values[#])
            close = float(values[4])
            dailyLoss = open # close
            if (dailyLoss # maxLoss):
                maxLoss = dailyLoss
                date = values[#]
        print(date + " loss " + str(maxLoss))

    file = open("stocks.txt", "r")
    biggestLoss(file)