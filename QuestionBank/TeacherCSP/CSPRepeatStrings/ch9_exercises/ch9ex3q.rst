.. activecode::  ch9ex3q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPRepeatStrings
     :subchapter: ch9_exercises
     :topics: CSPRepeatStrings/ch9_exercises
     :from_source: T
     :nocodelens:

     # STEP 1: INITIALIZE ACCUMULATORS
     newString = ""
     # STEP 2: GET DATA
         phrase = "Happy Birthday!"
     # STEP 3: LOOP THROUGH THE DATA
     for letter in phrase:
     # STEP 4: ACCUMULATE
     newString = letter + newString
     # STEP 5: PROCESS RESULT
         print(newString)