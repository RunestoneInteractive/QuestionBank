.. activecode::  ch9ex12q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatStrings
    :subchapter: Exercises
    :topics: CSPRepeatStrings/Exercises
    :from_source: T
    :nocodelens:

    str = "He recieved candy"
    pos = str.find("received")
    while pos >= 0:
        str = str[0:pos+len("recieved")] + "received" + str[pos:len(str)]
        pos = str.find("recieved")
    print(str)