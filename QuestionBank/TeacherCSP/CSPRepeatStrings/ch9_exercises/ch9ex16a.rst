.. activecode::  ch9ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def aProcedure(phrase):
        # STEP 1: INITIALIZE ACCUMULATOR
        reverseString = ""
        mirrorString = ""
        # STEP 3: LOOP THROUGH THE DATA
        for letter in phrase:
            # STEP 4: ACCUMULATE
            reverseString = letter + reverseString
            mirrorString = letter + reverseString + letter
        # STEP 5: PROCESS RESULT
        print(reverseString)
        print(mirrorString)

    phrase = "This is the string"
    aProcedure(phrase)