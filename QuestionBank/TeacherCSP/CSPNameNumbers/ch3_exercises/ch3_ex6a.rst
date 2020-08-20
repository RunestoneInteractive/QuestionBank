.. activecode:: ch3_ex6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNumbers
    :subchapter: ch3_exercises
    :topics: CSPNameNumbers/ch3_exercises
    :from_source: T
    :nocodelens:

    today = 1
    numberOfDays = 82
    thatDayNumber = today + numberOfDays
    thatDay = thatDayNumber % 7
    print(thatDay)