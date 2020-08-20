.. activecode::  ch13ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens

    state = "Georgia"
    if state == "Georgia" or state == "Florida":
        print("It's hot")
    elif state == "Alaska":
        print("It's cold")
    else:
        print("I don't know the weather")