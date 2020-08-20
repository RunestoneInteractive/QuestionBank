.. activecode::  ch17ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    def aProcedure(aString):
        aList = aString.split(",")
        agePart = aList[1]
        namePart = aList[0]
        verbPart = aList[2]

        posName = namePart.find("name:")
        posAge = agePart.find("age:")
        posVerb = verbPart.find("verb:")

        if (posName > -1):
            name = namePart[posName+6:len(namePart)]
        else:
            name = "Unknown"

        if (posAge > -1):
            age = agePart[posAge+5:len(agePart)]
        else:
            age = "Unknown"

        if (posVerb > -1):
            verb = verbPart[posVerb+6:len(verbPart)]
        else:
            verb = "Unknown"

        print(name + " who is " + age + " likes to " + verb)

    aProcedure("name: Bob,age: 10,verb: dance")