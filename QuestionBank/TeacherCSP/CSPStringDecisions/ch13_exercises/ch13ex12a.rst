.. activecode::  ch13ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    user = input("Give me a number")
    number = int(user)
    if number < 5:
        user2 = input("Give me a number")
        number2 = int(user2)
        if number2 > 3:
            print("I love CS")
        elif number2 < 3:
            print("CS is the best")
        else:
            print("I like CS better than food")
    else:
        print("Who else loves CS?")