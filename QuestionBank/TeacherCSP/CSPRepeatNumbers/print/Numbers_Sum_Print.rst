.. activecode:: Numbers_Sum_Print
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: print
    :topics: CSPRepeatNumbers/print
    :from_source: T
    :tour_1: "Code tour"; 2: accL_line2; 4: accL_line4; 5: accL_line5; 7: accL_line7; 8: accL_line8; 10: accL_line10; 12: accL_line12;

    # STEP 1: INITIALIZE ACCUMULATOR
    sum = 0  # Start out with nothing
    # STEP 2: GET DATA
    numbers = range(0,101,2)
    print("All the numbers:",numbers)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
        print("Number:",number)
        # STEP 4: ACCUMULATE
        sum = sum + number
    # STEP 5: PROCESS RESULT
    print(sum)