.. activecode:: ch18ex1q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPWebData
    :subchapter: Exercises
    :topics: CSPWebData/Exercises
    :from_source: T
    :nocodelens:

    inFile = open("uspoll.txt","r)
    line = inFile.readLine()
    while line
        values = line.split(":")
        city = values[0]
        if (city.find("A") == 0):
            print('City: ' city)
            print("Pollution values:",values[1],values[2])
        line = infile.readline()

    inFile.close()