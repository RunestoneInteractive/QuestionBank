.. activecode::  ch13ex14q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    if bikes > people:
    print("We should take the bikes.")
    if bikes < people:
    print("We should not take the bikes.")
    if bikes == people:
    print("We can't decide.")

    if vans > bikes:
    print("That's too many vans.")
    if vans < bikes:
    print("Maybe we could take the vans.")
    if vans == bikes:
    print("We still can't decide.")

    if people > vans:
    print("Alright, let's just take the vans.")
    if people <= vans:
    print("Fine, let's stay home then.")