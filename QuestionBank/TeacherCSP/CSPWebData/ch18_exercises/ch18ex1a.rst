.. activecode:: ch18ex1a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWebData
    :subchapter: ch18_exercises
    :topics: CSPWebData/ch18_exercises
    :from_source: T
    :nocodelens:

    inFile = open("uspoll.txt","r")
    line = inFile.readline()
    while line:
        values = line.split(":")
        city = values[0]
        if (city.find("A") == 0):
            print('City: ', city)
            print("Pollution values:",values[1],values[2])
        line = inFile.readline()

    inFile.close()