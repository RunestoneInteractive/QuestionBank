.. parsonsprob:: listMixed_rainfall
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-MixedupCode
    :topics: 08-lists/08-MixedupCode
    :from_source: T
    :numbered: left
    :adaptive:
    :practice: T

    Let's imagine that you have a list that contains amounts of rainfall for each day, collected by a
    meteorologist. Her rain gathering equipment occasionally makes a mistake and reports a negative
    amount for that day. We have to ignore those. We need to write a program to (a) calculate the total
    rainfall by adding up all the positive integers (and only the positive integers), (b) count the number
    of positive integers (we will count with "1.0" so that our average can have a decimal point), and (c)
    print out the average rainfall at the end. Only print the average if there was some rainfall, otherwise
    print "No rain". Construct a program that correctly solves the rainfall problem. Watch out for extra
    code blocks and indentation!
    -----
    rain = [0,5,1,0,-1,6,7,-2,0]
    sumRain = 0
    count = 0
    =====
    for day in rain:
    =====
    for day in rain #distractor
    =====
        if day >= 0:
    =====
            sumRain = sumRain + day
            count = count + 1.0
    =====
    if count > 0:
    =====
        ave = sumRain / count
        print("Average",ave)
    =====
    else:
    =====
    else #distractor
    =====
        print("No rain")