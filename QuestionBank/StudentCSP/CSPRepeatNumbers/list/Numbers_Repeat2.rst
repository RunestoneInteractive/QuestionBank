.. activecode:: Numbers_Repeat2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatNumbers
    :subchapter: list
    :topics: CSPRepeatNumbers/list
    :from_source: T
    :tour_1: "Line by line tour"; 1: for1_line1; 2: for1_line2; 3: for1_line3; 4: for1_line4; 5: for1_line5;
    :tour_2: "High level tour"; 1-2: for1_line1-2; 3-4: for1_line3-4; 5: for1_s_line5;

    sum = 0  # Start out with nothing
    thingsToAdd = [1,2,3,4,5,6,7,8,9,10]
    for number in thingsToAdd:
        sum = sum + number
    print(sum)