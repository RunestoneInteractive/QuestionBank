.. activecode::  ch4ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameStrings
    :subchapter: ch4_exercises
    :topics: CSPNameStrings/ch4_exercises
    :from_source: T
    :nocodelens:

    s1 = "hi"
    s2 = "My namesake is Bob, and he and I love to eat ham."
    s3 = s1.capitalize()
    s4 = s2[0:7].lower()
    s5 = s2[12:18]
    s6 = s2[31:33]
    s7 = s2[46:48]
    s8 = len(s1)
    print(s3 + " " + s4 + " " + s5 + " " + s6 + s7 + " " + str(s8))