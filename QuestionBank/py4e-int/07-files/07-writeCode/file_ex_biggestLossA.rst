.. activecode:: file_ex_biggestLossA
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :optional:

    def biggestLoss(file):
        maxLoss = 0
        lines = file.readlines()
        for line in lines:
            values = line.split(",")
            opening = float(values[1])
            closing = float(values[4])
            dailyLoss = opening - closing
            if (dailyLoss < maxLoss):
                maxLoss = dailyLoss
                date = values[0]
        print(date + " loss " + str(maxLoss))

    file = open("stocks.txt", "r")
    biggestLoss(file)