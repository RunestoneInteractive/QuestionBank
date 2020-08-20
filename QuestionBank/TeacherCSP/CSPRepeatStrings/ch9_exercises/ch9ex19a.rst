.. activecode::  ch9ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def encode2(message, eStr):
        str = "abcdefghijklmnopqrstuvwxyz. "
        encodedMessage = ""
        for letter in message:
            pos = str.find(letter)
            encodedMessage = encodedMessage + eStr[pos:pos+1]
        return(encodedMessage)

    print(encode2("This is a test", "zyxwvutsrqponmlkjihgfedcba ."))