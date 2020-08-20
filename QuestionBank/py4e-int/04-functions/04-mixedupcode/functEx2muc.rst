.. parsonsprob:: functEx2muc
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-mixedupcode
    :topics: 04-functions/04-mixedupcode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    Create a function called bmi that takes height and weight as parameters. It should return BMImetric.
    Watch your indentation.
    -----
    def bmi(height, weight):
    =====
        heightSquared = height * height
    =====
        BMI = weight / heightSquared
    =====
        BMImetric = BMI * 703
    =====
        return BMImetric