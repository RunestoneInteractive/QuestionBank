.. activecode::  ch9ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def encode(message):
        str = "abcdefghijklmnopqrstuvwxyz. "
        eStr = "zyxwvutsrqponmlkjihgfedcba ."
        encodedMessage = ""
        for letter in message:
            pos = str.find(letter)
            encodedMessage = encodedMessage + eStr[pos:pos+1]
        return(encodedMessage)

    print(encode("The password is touchdown."))