.. parsonsprob:: cndtnl-try-pp-temp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-tryExcept
    :topics: 03-conditional/03-tryExcept
    :from_source: T
    :practice: T
    :adaptive:
    :numbered: left

    The following program should get a temperature in Fahrenheit from the user, then print out the
    temperature in Celsius. If the input is not a number, it should ask the user to enter a
    number again. Be sure to indent correctly!
    -----
    inp = input('Enter Fahrenheit Temperature:')
    =====
    try:
    =====
        fahr = float(inp)
    =====
        fahr = int(inp) #paired
    =====
        cel = (fahr - 32.0) * 5.0 / 9.0
    =====
        print(cel)
    =====
    except:
    =====
        print('Please enter a number')