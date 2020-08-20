.. activecode:: Numbers_Product2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatNumbers
    :subchapter: range
    :topics: CSPRepeatNumbers/range
    :from_source: T
    :tour_1: "Line by line tour"; 1: for2_line1; 2: for2_line2; 3: for2_line3; 4: for2_line4; 5: for2_line5;

    product = 1  # Start out with nothing
    numbers = range(1,11)
    for number in numbers:
        product = product * number
    print(product)