.. activecode:: Sum_Numbers
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroData
    :subchapter: workLists
    :topics: CSPIntroData/workLists
    :from_source: T
    :tour_1: "Line by line tour"; 2: for1_line1; 3: for1_line2; 6: for1_line3; 7: for1_line4; 10: for1_line5;
    :tour_2: "High level tour"; 2-3: for1_line1-2; 6-7: for1_line3-4; 10: for1_s_line5;

    # initialize the variables
    sum = 0
    thingsToAdd = [1,2,3,4,5,6,7,8,9,10]

    # loop through the list and add each value to the sum
    for number in thingsToAdd:
        sum = sum + number

    # print the sum
    print(sum)