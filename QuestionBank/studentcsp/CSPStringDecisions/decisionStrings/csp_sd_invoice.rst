.. activecode:: csp_sd_invoice
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPStringDecisions
    :subchapter: decisionStrings
    :topics: CSPStringDecisions/decisionStrings
    :from_source: T
    :tour_1: "Structural Tour"; 1: sd1line1; 2-3: sd1line2-3; 4-5: sd1line4-5; 6: sd1line6;

    numItems = 1
    if numItems == 1:
        message = "You ordered 1 item"
    if numItems > 1:
        message = "You ordered " + str(numItems) + " items"
    print(message)