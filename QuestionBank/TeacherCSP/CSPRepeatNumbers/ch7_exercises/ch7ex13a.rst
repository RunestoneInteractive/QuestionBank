.. activecode::  ch7ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    # STEP 1: INITIALIZE ACCUMULATOR
    product = 1  # init product to 1
    # STEP 2: GET DATA
    numbers = range(10,21,2)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
        # STEP 4: ACCUMULATE
       product = product * number
    # STEP 5: PROCESS RESULT
    print(product)