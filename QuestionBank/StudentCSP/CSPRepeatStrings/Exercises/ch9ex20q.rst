.. activecode::  ch9ex20q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatStrings
    :subchapter: Exercises
    :topics: CSPRepeatStrings/Exercises
    :from_source: T
    :nocodelens:

    message = "meet me at midnight"
    str = "abcdefghijklmnopqrstuvwxyz. "
    eStr = "zyxwvutsrqponmlkjihgfedcba ."
    encodedMessage = ""
    for letter in message:
        pos = str.find(letter)
        encodedMessage = encodedMessage + eStr[pos:pos+1]
    print(encodedMessage)