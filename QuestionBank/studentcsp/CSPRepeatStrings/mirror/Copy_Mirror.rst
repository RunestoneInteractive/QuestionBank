.. activecode:: Copy_Mirror
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatStrings
    :subchapter: mirror
    :topics: CSPRepeatStrings/mirror
    :from_source: T
    :tour_1: "Lines of code"; 2: strR3-line1; 4: strR3-line2; 6: strR3-line3; 8: strR3-line4; 10: strR3-line5;

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