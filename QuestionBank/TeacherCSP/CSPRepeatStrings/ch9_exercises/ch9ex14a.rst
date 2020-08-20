.. activecode::  ch9ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    str = "I like to eat. sleep. learn. and code!"
    pos = str.find(".")
    while pos >= 0:
        str = str[0:pos] + "," + str[pos+len("."):len(str)]
        pos = str.find(".")
    print(str)