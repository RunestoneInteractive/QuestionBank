.. activecode::  ch8ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def calculateAverage():
        sum = 0
        count = 0
        message = "Enter an integer or a negative number to stop"
        value = input(message)
        while int(value) > 0:
            print("You entered " + value)
            sum = sum + int(value)
            count = count + 1
            value = input(message)
        return(sum / count)

    print(calculateAverage())