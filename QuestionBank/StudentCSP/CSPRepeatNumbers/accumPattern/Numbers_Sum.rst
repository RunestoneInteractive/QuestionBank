.. activecode:: Numbers_Sum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatNumbers
    :subchapter: accumPattern
    :topics: CSPRepeatNumbers/accumPattern
    :from_source: T
    :tour_1: "Code tour"; 2: accum_line2; 4: accum_line4; 6: accum_line6; 8: accum_line8; 10: accum_line10;

    # STEP 1: INITIALIZE ACCUMULATOR
    sum = 0  # Start out with nothing
    # STEP 2: GET DATA
    numbers = range(1,101)
    # STEP 3: LOOP THROUGH THE DATA
    for number in numbers:
        # STEP 4: ACCUMULATE
        sum = sum + number
    # STEP 5: PROCESS RESULT
    print(sum)