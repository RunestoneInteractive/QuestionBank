.. activecode:: Invoice1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNumbers
    :subchapter: invoice
    :topics: CSPNameNumbers/invoice
    :from_source: T
    :tour_1: "Line by line tour"; 1: inv-line1; 2: inv-line2; 3: inv-line3; 4: inv-line4; 5: inv-line5; 6: inv-line6; 7: inv-line7; 8: inv-line8;

    quantity1 = 2
    unitPrice1 = 7.56
    total1 = quantity1 * unitPrice1
    quantity2 = 4
    unitPrice2 = 4.71
    total2 = quantity2 * unitPrice2
    invoiceTotal = total1 + total2
    print(invoiceTotal)