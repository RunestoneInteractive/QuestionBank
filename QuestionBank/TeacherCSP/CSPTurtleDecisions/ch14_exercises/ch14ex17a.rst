.. activecode::  ch14ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPTurtleDecisions
    :subchapter: ch14_exercises
    :topics: CSPTurtleDecisions/ch14_exercises
    :from_source: T
    :nocodelens:

    def getColor(num):
        if num % 3 == 0:
            return 'yellow'
        elif num % 3 == 1:
            return 'blue'
        else:
            return 'green'

    print(getColor(3))
    print(getColor(4))
    print(getColor(5))
    print(getColor(6))