.. parsonsprob:: cndtnl-mixed-hi
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-MixedupCode
    :topics: 03-conditional/03-MixedupCode
    :from_source: T
    :adaptive:
    :practice: T
    :numbered: left

    The following program should prints “Hello” if x is less than 2, "Hey" if x is greater than 2,
    and "Hi" if x is 2. Be sure to indent correctly and look out for extra code blocks!
    -----
    x = 2
    =====
    if x < 2:
    =====
    if x < 2 #paired
    =====
        print ("Hello")
    =====
    elif x > 2:
    =====
    else x > 2: #paired
    =====
        print ("Hey")
    =====
    else:
    =====
        print ("Hi")
    =====
        print "Hi" #paired
    =====
    elif x >= 2: #distractor