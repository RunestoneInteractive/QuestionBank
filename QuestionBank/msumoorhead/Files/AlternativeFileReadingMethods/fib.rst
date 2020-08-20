.. activecode:: fib
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Files
    :subchapter: AlternativeFileReadingMethods
    :topics: Files/AlternativeFileReadingMethods
    :from_source: None
    :nocodelens:

    infile = open("qbdata.txt", "r")
    line = infile.readline()
    while line:
        values = line.split()
        passes = int(values[4]) + int(values[5]) + int(values[8])
        print('{} {} made {} passes'.format(values[0], values[1], passes))
        line = infile.readline()

    infile.close()