.. activecode::  ch9ex17q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPRepeatStrings
     :subchapter: Exercises
     :topics: CSPRepeatStrings/Exercises
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