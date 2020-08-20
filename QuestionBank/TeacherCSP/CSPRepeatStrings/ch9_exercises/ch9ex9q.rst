.. activecode::  ch9ex9q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPRepeatStrings
     :subchapter: ch9_exercises
     :topics: CSPRepeatStrings/ch9_exercises
     :from_source: T
     :nocodelens:

     message = "meet me at midnight"
     str = "abcdefghijklmnopqrstuvwxyz.
     eStr = zyxwvutsrqponmlkjihgfedcba ."
     encodedMessage = message
     for letter in message
         pos = str.find(letter)
         encodedMessage = encodedMessage + eStr[pos:pos+1]
     print encodedMessage)