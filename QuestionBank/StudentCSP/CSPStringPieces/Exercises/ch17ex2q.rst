.. activecode::  ch17ex2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPStringPieces
    :subchapter: Exercises
    :topics: CSPStringPieces/Exercises
    :from_source: T
    :nocodelens:

    # create the input
    input = "Pat,Smith,girl,65 Elm Street,eat'

    # split on the comma
    pieces = input.split(,)

    # print the values
    print("First name is:" + pieces)
    print("Last name is:" + pieces[2])