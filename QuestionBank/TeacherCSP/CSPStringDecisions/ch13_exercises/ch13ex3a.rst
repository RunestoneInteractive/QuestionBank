.. activecode::  ch13ex3a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringDecisions
    :subchapter: ch13_exercises
    :topics: CSPStringDecisions/ch13_exercises
    :from_source: T
    :nocodelens:

    print("You are in front of a creepy door in a hallway.")
    print("What do you want to do?")
    action = input ("Type: in, left, or right. Then click OK or press enter")
    if action == "in":
        print("You choose to go in.")
        print("The room is pitch black.")
    if action == "left":
        print("You choose to turn left.")
        print("A ghost appears at the end of the hall.")
    if action == "right":
        print("You choose to turn right.")
        print("A greenish light is visible in the distance.")