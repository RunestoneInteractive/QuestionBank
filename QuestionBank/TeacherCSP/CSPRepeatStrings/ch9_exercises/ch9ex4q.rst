.. activecode::  ch9ex4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    # STEP 2: GET DATA
    phrase = "Hey look, I'm a string!"
    # STEP 3: LOOP THROUGH THE DATA
    for letter in phrase:
        newString = ""
        # STEP 4: ACCUMULATE
        newString = newString + phrase
        # STEP 5: PROCESS RESULT
        print(phrase)