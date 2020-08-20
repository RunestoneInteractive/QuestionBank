.. activecode::  ch18ex13q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPWebData
    :subchapter: Exercises
    :topics: CSPWebData/Exercises
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