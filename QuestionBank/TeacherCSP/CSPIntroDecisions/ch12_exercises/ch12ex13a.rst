.. activecode::  ch12ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens

    score = 93
    if score >= 90:
        grade = "A"
    if score >= 80 and score <= 89:
        grade = "B"
    if score >= 70 and score <= 79:
        grade = "C"
    if score >= 60 and score <= 69:
        grade = "D"
    if score < 60:
       grade = "E"
    print(grade)