.. activecode::  ch9ex17q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPRepeatStrings
     :subchapter: ch9_exercises
     :topics: CSPRepeatStrings/ch9_exercises
     :from_source: T
     :nocodelens:

     message = ""
     str = "abcdefghijklmnopqrstuvwxyz. "
     eStr = "zyxwvutsrqponmlkjihgfedcba ."
     encodedMessage = "nvvg.nv.zg.nrwmrtsg"
     for letter in encodedMessage:
         pos = eStr.find(letter)
         message = message + str[pos:pos+1]
     print(message)