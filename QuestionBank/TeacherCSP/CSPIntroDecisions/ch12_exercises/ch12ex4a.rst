.. activecode::  ch12ex4a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens:

    weight = .5

    if weight >= 1:
        price = 4
    if weight < 1:
        price = 2
    total = weight * price
    print(total)