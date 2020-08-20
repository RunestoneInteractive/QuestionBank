.. activecode::  file_ex_AorBq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:
    :available_files: uspoll.txt

    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # loop through the lines
    for line in lines:
        if line[0] == "A":
            print(line)