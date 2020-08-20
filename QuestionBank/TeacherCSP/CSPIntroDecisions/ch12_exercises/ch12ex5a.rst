.. activecode::  ch12ex5a
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
    if weight < 2:
        price = 1.50
    if weight >= 2:
        price = 1.30
    total = weight * price
    print(weight)
    print(price)
    print(total)