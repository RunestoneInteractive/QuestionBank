.. activecode::  ch8ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def printSquare(numStars):
        for x in range(0,numStars):
            line = ""
            for y in range(0,numStars):
                line = line + ' *'
            print(line)

    printSquare(6)