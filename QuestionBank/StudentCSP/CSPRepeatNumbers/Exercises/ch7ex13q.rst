.. activecode::  ch7ex13q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPRepeatNumbers
     :subchapter: Exercises
     :topics: CSPRepeatNumbers/Exercises
     :from_source: T
     :nocodelens:

     # STEP 1: INITIALIZE ACCUMULATOR
     product = 0  # init product
     # STEP 2: GET DATA
     numbers = range(10,20,2)
     # STEP 3: LOOP THROUGH THE DATA
     for number in numbers:
         # STEP 4: ACCUMULATE
        product = product + number
     # STEP 5: PROCESS RESULT
     print(product)