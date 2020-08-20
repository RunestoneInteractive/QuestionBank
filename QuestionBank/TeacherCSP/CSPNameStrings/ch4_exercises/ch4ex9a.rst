.. activecode::  ch4ex9a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameStrings
    :subchapter: ch4_exercises
    :topics: CSPNameStrings/ch4_exercises
    :from_source: T
    :nocodelens:

    numPeople = 5
    amountPerPerson = 4
    price = 0.5
    total = numPeople * amountPerPerson
    numWings = total / price
    print("You can order " + str(numWings) + " wings" +
          " when you have " + str(numPeople) + " people" +
          " who can each spend " + str(amountPerPerson) + " dollars" +
          " and wings cost " + str(price) + " each.")