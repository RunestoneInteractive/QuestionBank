.. parsonsprob:: cndtnl-mixed-grade
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-MixedupCode
    :topics: 03-conditional/03-MixedupCode
    :from_source: T
    :practice: T
    :adaptive:
    :numbered: left

    Arrange the code to print the grade equivalent (string) for a score. It should return E for any value
    below 60, D for 61 to 69, C for 70 to 79, B for 80 to 89 and A for 90 and above.
    -----
    score = 93
    =====
    if score >= 90:
    =====
        grade = "A"
    =====
    elif score >= 80:
    =====
        grade = "B"
    =====
    elif score >= 70:
    =====
        grade = "C"
    =====
    elif score >= 60:
    =====
        grade = "D"
    =====
    else:
    =====
        grade = "E"
    =====
    print(grade)
    =====
        elif grade >= 90: #distractor
    =====
        score = "c" #distractor