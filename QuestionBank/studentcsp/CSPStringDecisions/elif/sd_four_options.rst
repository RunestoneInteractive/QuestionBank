.. activecode:: sd_four_options
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPStringDecisions
    :subchapter: elif
    :topics: CSPStringDecisions/elif
    :from_source: T
    :tour_1: "Structural Tour"; 1: sd7-line1; 2-3: sd7-line2-3; 4-5: sd7-line4-5; 6-7: sd7-line6-7; 8-9: sd7-line8-9;

    x = .25
    if x <= .25:
        print("x is in the first quartile - x <= .25")
    elif x <= .5:
        print("x is in the second quartile - .25 < x <= .5")
    elif x <= .75:
        print("x is in the third quartile - .5 < x <= .75")
    else:
        print("x is in the fourth quartile - .75 < x <= 1")