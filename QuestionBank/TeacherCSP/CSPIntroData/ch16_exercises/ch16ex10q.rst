.. activecode::  ch16ex10q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    # setup the source list
    source = ["This","is","a","list"]

    # Set the accumulator to the empty list
    soFar = []

    # Loop through all the items in the source list
    for index in range(0,len(source)):

        # Add a list with the current item from source to soFar
        soFar =  [source[index]] + soFar
    print(soFar)