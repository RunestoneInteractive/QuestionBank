.. activecode::  ch4ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameStrings
    :subchapter: ch4_exercises
    :topics: CSPNameStrings/ch4_exercises
    :from_source: T
    :nocodelens:

    user = input("Type a sentence")
    user = user.lower()
    length = len(user)
    print("The length of " + user + " is" + str(length))