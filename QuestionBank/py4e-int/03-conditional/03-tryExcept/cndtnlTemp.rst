.. activecode:: cndtnlTemp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-tryExcept
    :topics: 03-conditional/03-tryExcept
    :from_source: T
    :caption: Temperature converter

    inp = input('Enter Fahrenheit Temperature: ')
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)