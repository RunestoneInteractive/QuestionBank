.. activecode::  file_ex_pmErrorq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:
    :available_files: uspoll.txt

    Fix the errors in the code below so that it prints the average PM values
    of only the cities that start with "A".
    ~~~~
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    total25 = 0
    count = 1.0
    for line in lines:
        values = line.split(":")
        new25 = float(values[2])
        city = values[1]
        if (city.find("A") == -1):
            total25 = total25 + new25
        count = count + 1

    print("Average PM 2.5 value for cities that start with 'A' is ", total25/count)