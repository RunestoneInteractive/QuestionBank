.. activecode::  ch9ex5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    # STEP 1: INITIALIZE ACCUMULATOR
    newString = ""
    # STEP 2: GET DATA
    phrase = "This is a test"
    # STEP 3: LOOP THROUGH THE DATA
    for letter in phrase:
        # STEP 4: ACCUMULATE
        newString = letter + newString + letter
    # STEP 5: PROCESS RESULT
    print(newString)