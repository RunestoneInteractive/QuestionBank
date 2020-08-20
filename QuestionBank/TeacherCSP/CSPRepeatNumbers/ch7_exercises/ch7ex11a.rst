.. activecode::  ch7ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def sumEvens(lastNum):
        # STEP 1: INITIALIZE ACCUMULATOR
        sum = 0  # Start out with nothing
        # STEP 2: GET DATA
        numbers = range(0,lastNum+1,2)
        # STEP 3: LOOP THROUGH THE DATA
        for number in numbers:
            # STEP 4: ACCUMULATE
            sum = sum + number
        # STEP 5: PROCESS RESULT
        return(sum)

    print(sumEvens(20))