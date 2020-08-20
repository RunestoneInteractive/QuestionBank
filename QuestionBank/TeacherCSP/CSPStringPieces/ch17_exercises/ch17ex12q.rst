.. activecode::  ch17ex12q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    agePart = "Their age: 17"
    posAge = agePart.find("age:")
    if (posAge < 0):
        age = agePart[posAge:len(agePart)]
    else:
        age = "Unknown"
    print(age)