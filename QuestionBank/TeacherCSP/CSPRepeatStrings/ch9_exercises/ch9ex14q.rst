.. activecode::  ch9ex14q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    str = "I like to eat. sleep. learn. and code!"
    pos = str.
    while pos >= :
        str = str[0:pos] +   + str[  :len(str)]
        pos =
    print(str)