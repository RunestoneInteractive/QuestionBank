.. activecode::  ch9ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: ch9_exercises
    :topics: CSPRepeatStrings/ch9_exercises
    :from_source: T
    :nocodelens:

    def decode(eMessage):
        message = ""
        str = "abcdefghijklmnopqrstuvwxyz. "
        eStr = "zyxwvutsrqponmlkjihgfedcba ."
        for letter in eMessage:
            pos = eStr.find(letter)
            message = message + str[pos:pos+1]
        return(message)

    print(decode("nvvg.nv.zg.nrwmrtsg"))