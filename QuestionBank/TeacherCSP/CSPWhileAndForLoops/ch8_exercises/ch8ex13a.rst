.. activecode::  ch8ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    # STEP 1: INITIALIZE ACCUMULATOR
    product = 1  # init product to 1
    # STEP 2: INIT THE DATA
    number = 10
    # STEP 3: LOOP THROUGH THE DATA
    while number < 21:
        # STEP 4: ACCUMULATE
        product = product * number
        # STEP 5: change the number
        number = number + 2
    # STEP 6: PROCESS RESULT
    print(product)