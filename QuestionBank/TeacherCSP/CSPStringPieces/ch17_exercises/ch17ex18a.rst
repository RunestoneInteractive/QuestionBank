.. activecode::  ch17ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    def aSentence(name, age, verb1, verb2):
        if age < 10:
            print(name + " who is " + str(age) + " " + verb1)
        else:
            print(name + " who is " + str(age) + " " + verb1)
    aSentence("John", 10, "runs", "sleeps")