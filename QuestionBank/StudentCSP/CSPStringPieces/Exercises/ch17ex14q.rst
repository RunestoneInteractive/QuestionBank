.. activecode::  ch17ex14q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPStringPieces
    :subchapter: Exercises
    :topics: CSPStringPieces/Exercises
    :from_source: T
    :nocodelens:

    agePart = "Their age: 17"
    posAge = agePart.find("age:")
    if (posAge > -1):
        age = agePart[posAge+5:len(agePart)]
    else:
        age = "Unknown"
    print(age)

    namePart = "name: Anu Gao"
    posName = namePart.find("name:")
    if (posName > -1):
        name = namePart[posName+6:len(namePart)]
    else:
        name = "Unknown"
    print(name)