.. activecode::  cndtnl-wc-distancea
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T
    :optional:
    :nocodelens:

    distance = 14
    # SET CONDITIONS
    if distance <= 12:
        rate = 2.00
    if distance > 12:
        rate = 1.50
    # CALCULATE TRIP COST
    total = distance * rate
    print("Total cost of trip: " + str(total))