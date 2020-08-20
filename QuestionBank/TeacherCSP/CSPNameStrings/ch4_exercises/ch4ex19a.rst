.. activecode::  ch4ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameStrings
    :subchapter: ch4_exercises
    :topics: CSPNameStrings/ch4_exercises
    :from_source: T
    :nocodelens:

    place = input("Enter the name of a place.")
    verb = input("Enter a verb.")
    action = input("Enter an action.")
    color = input("Enter your favorite color.")
    animal = input("What is your favorite animal?")
    print("Once upon a time in " + place + ", I was " +
          verb + "ing and I " + action + " because a " +
          color + " " + animal + " was also " + verb + "ing.")