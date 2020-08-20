.. activecode::  ch17ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    input = "Barb, horse, Sport, tall"
    pieces = input.split(",")
    name = pieces[0]
    animal = pieces[1]
    animalName = pieces[2]
    description = pieces[3]
    line1 = "Once upon a time there was a girl named, " + name + "."
    line2 = "She had a " + description + " " + animal + " named " + animalName + "."
    print(line1)
    print(line2)