.. activecode::  ch7ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    def letterCombiner(letterList):
            tempString = ""
            for letter in letterList:
                    tempString = tempString + letter
            return tempString

    aList = ["H", "i"]
    print(letterCombiner(aList))