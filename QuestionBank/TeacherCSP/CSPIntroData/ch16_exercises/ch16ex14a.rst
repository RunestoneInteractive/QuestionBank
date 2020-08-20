.. activecode::  ch16ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    # initialize the variables
    source = ["This","is","a","list"]
    newList = []

    # loop from the last index to the first (0)
    for index in range(len(source) - 1, -1, -1):

        # append the lists
        newList = [source[index]] + newList

    # print the current value of the list
    print(newList)