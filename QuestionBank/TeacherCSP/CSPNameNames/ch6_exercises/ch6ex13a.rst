.. activecode::  ch6ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def calcNumMiles(tankCapacity,amountLeft, milesPerGallon):
        numGallons = tankCapacity * amountLeft
        numMiles = numGallons * milesPerGallon
        return(numMiles)

    print("The number of miles you can go is " + str(calcNumMiles(10,0.25,32)))