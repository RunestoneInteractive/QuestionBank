.. activecode::  ch12ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: ch12_exercises
    :topics: CSPIntroDecisions/ch12_exercises
    :from_source: T
    :nocodelens:

    def aProcedure(price, wallet):
        if (wallet - price) >= 0:
            print("You have enough money")
        else:
            print("Get more money")

    aProcedure(10, 20)