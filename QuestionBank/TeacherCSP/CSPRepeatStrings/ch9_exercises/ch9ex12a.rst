.. activecode::  ch9ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    str = "He recieved candy"
    pos = str.find("recieved")
    while pos >= 0:
        str = str[0:pos] + "received" + str[pos+len("recieved"):len(str)]
        pos = str.find("recieved")
    print(str)