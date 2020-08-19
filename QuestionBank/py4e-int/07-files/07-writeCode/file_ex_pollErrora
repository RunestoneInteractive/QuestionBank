.. activecode:: file_ex_pollErrora
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:
    :optional:
    :available_files: uspoll.txt

    inFile = open("uspoll.txt","r")
    line = inFile.readline()
    while line:
        values = line.split(":")
        city = values[0]
        if (city.find("A") == 0):
            print('City: ' + city)
            print("Pollution values:",values[1],values[2])
        line = inFile.readline()

    inFile.close()