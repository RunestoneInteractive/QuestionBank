.. activecode::  ch9ex10a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    str = "Th1s is a str1ng"
    pos = str.find("1")
    while pos >= 0:
        str = str[0:pos] + "i" + str[pos+1:len(str)]
        pos = str.find("1")
    print(str)