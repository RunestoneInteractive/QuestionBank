.. activecode::  ch12ex12q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens:

    weight = 0.5
    numItems = 5
    wallet = 2

    if weight < 1:
        price = 1.45
        if weight >= 1:
        price = 1.15
        total = numItems * price
        if total > wallet:
        print("You have no money")