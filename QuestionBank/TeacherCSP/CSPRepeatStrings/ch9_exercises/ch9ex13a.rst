.. activecode::  ch9ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def mirror(phrase):

        # STEP 1: INITIALIZE ACCUMULATOR
        newString = ""
        # STEP 3: LOOP THROUGH THE DATA
        for letter in phrase:
            # STEP 4: ACCUMULATE
            newString = letter + newString + letter
        # STEP 5: PROCESS RESULT
        return(newString)

    print(mirror("Hi Class!"))