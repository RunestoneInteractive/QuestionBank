.. activecode::  ch17ex2a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    # create the input
    input = "Pat,Smith,girl,65 Elm Street,eat"

    # split on the comma
    pieces = input.split(",")

    # print the values
    print("First name is:" + pieces[0])
    print("Last name is:" + pieces[1])