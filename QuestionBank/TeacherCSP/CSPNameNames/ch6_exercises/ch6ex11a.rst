.. activecode::  ch6ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def costOfTrip(miles, milesPerGallon, pricePerGallon):
        numGallons = miles / milesPerGallon
        total = numGallons * pricePerGallon
        return(total)

    print("The cost of the trip is " + str(costOfTrip(500,26,3.45)))