.. activecode::  ch9ex10q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatStrings
    :subchapter: Exercises
    :topics: CSPRepeatStrings/Exercises
    :from_source: T
    :nocodelens:

    str = "Th1s is a str1ng"
    pos = str.find("1")
    while pos >= 0:
        pos = str.find("1")
        str = str[0:pos] + "i" + str[pos+1:len(str)]
    print(str)