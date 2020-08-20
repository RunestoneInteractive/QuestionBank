.. activecode::  ch6ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def printMadLib(place,verb,action,color,animal):
        print("Once upon a time in " + place + ", I was " +
              verb + "ing and I " + action + " because a " +
              color + " " + animal + " was also " + verb + "ing.")

    place = input("Enter the name of a place.")
    verb = input("Enter a verb.")
    action = input("Enter an action.")
    color = input("Enter your favorite color.")
    animal = input("What is your favorite animal?")
    printMadLib(place,verb,action,color,animal)