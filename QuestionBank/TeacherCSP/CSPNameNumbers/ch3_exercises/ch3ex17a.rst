.. activecode::  ch3ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNumbers
    :subchapter: ch3_exercises
    :topics: CSPNameNumbers/ch3_exercises
    :from_source: T
    :nocodelens:

    pricePerApple = 0.6
    numPears = 3
    pricePerPear = 1.2
    funds = 8
    fundsAfterPears = funds - (pricePerPear * numPears)
    numApples = fundsAfterPears / pricePerApple
    print(numApples)