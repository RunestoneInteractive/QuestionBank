.. activecode:: cndtnl-wc-leapYeara
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T
    :optional:

    year = 1900 #TEST WITH ANY YEAR
    # Initializing leapYear to False since most years are not leap years
    leapYear = False

    # Use modulus to see if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, use modulus to see if divisible by 100
        if year % 100 == 0:
            # if divisible by 4 and 100, use modulus to see if divisible by 400
            if year % 400 == 0:
                # if divisible by 4, 100, and 400 it is a leap year
                leapYear = True
        else: # if divisible by 4 and not 100 it is a leap year
            leapYear = True
    print(leapYear)
    ''' Since leapYear started as False, we do not need to reset it to False
        for the instances that the year is not a leap year '''

    # ANOTHER OPTION
    year = 1900
    leapYear = False
    if year % 400 == 0:
        leapYear = True
    elif year % 4 == 0 and year % 100 != 0:
        leapYear = True
    print(leapYear)