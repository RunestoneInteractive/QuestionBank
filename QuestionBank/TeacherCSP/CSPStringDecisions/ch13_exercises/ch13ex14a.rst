.. activecode::  ch13ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    people = 30
    bikes = 40
    vans = 15


    if bikes > people:
        print("We should take the bikes.")
    elif bikes < people:
        print("We should not take the bikes.")
    else:
        print("We can't decide.")

    if vans > bikes:
        print("That's too many vans.")
    elif vans < bikes:
        print("Maybe we could take the vans.")
    else:
        print("We still can't decide.")

    if people > vans:
        print("Alright, let's just take the vans.")
    else:
        print("Fine, let's stay home then.")