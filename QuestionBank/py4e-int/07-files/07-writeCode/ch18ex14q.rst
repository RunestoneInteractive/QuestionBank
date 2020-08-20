.. activecode::  ch18ex14q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:
    :available_files: stocks.txt

    def pointGain(file):
        lines = file.readlines()
        for lines in lines:
        values = line.split()
        open = str(values[2])
        close = float(values[4])
        if (close - open) < 300:
            print(values[0])
    file = open("stocks.txt", "r")
    pointGain(file)