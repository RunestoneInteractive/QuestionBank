.. activecode::  ch9ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
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

    decodedMessage = ""
    for letter in encodedMessage:
        pos = eStr.find(letter)
        decodedMessage = decodedMessage + str[pos:pos+1]
    print(decodedMessage)