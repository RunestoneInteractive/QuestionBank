.. activecode::  ch6ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def newTime(currentHour, currentMinute, intHour, intMinute):
            minutes = currentMinute + intMinute
            remainingMinutes = minutes % 60
            hoursFromMinutes = minutes - remainingMinutes
            newHour = (currentHour + intHour + hoursFromMinutes) % 12
            return (str(newHour) + " hour(s) and " + str(remainingMinutes) + " minute(s)")

    print(newTime(1, 30, 5, 50))