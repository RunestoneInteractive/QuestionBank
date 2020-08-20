.. activecode::  ch16ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: ch16_exercises
    :topics: CSPIntroData/ch16_exercises
    :from_source: T
    :nocodelens:

    # initialize the variables
    numbers = range(1,51,5)
    fives = []

    # loop though every index
    for index in range(0,len(numbers)):

        # add the lists
        fives = fives + [numbers[index]]

    # print the result
    print(fives)