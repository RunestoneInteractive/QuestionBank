.. activecode::  ch18ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    def avgChange(file):
        lines = file.readlines()
        gainSum = 0
        gainCounter = 0
        lossSum = 0
        lossCounter = 0
        for line in lines:
            values = line.split(",")
            open = float(values[1])
            close = float(values[4])
            change = close - open
            if change >= 0:
                gainSum = gainSum + change
                gainCounter += 1
            else:
                change = change * -1
                lossSum = lossSum + change
                lossCounter += 1
        return (gainSum/gainCounter) - (lossSum/lossCounter)

    file = open("stocks.txt", "r")
    print(avgChange(file))