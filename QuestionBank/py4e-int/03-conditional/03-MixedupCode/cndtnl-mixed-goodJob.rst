.. parsonsprob:: cndtnl-mixed-goodJob
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

    The following program should print "Good job" when the number is between 1 and 10 (inclusive) or is 15
    and "Fail" when it is not. Be sure to indent correctly and watch out for extra pieces of code!
    -----
    x = 8
    =====
    if x >= 1 and x <= 10 or x == 15:
    =====
    print("Good job")
    =====
    else:
    =====
    print("Fail")
    =====
    elif x == 15: #distractor