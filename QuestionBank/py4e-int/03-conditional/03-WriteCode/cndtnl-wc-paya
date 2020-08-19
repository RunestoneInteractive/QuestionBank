.. activecode:: cndtnl-wc-paya
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T
    :optional:

    #initializing variables
    hours = 45
    rate = 10
    overtimeRate = rate * 1.5
    grossPay = 0

    #starting if statement to see if hours are within regular pay
    if hours <= 40:
        #if within 40 hours, pay will be hours * rate
        grossPay = hours * rate
    #else statement if hours are greater than 40
    else:
        #creating a variable for overtime hours
        overTime = hours % 40
        #pay will equal the regular rate for 40 hours, plus the overtime rate for the extra hours
        grossPay = (rate * 40) + (overTime * overtimeRate)
    print(grossPay)