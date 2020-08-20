.. activecode::  ch9ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def reverse(phrase):
        # STEP 1: INITIALIZE ACCUMULATORS
        newString = ""

        # STEP 3: LOOP THROUGH THE DATA
        for letter in phrase:

           # STEP 4: ACCUMULATE
           newString = letter + newString

        # STEP 5: PROCESS RESULT
        return(newString)

    print(reverse("Happy Birthday!"))