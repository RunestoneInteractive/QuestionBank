.. activecode::  ch8ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: ch8_exercises
    :topics: CSPWhileAndForLoops/ch8_exercises
    :from_source: T
    :nocodelens:

    def inputFunc():
        userInput = input("Give me a string")
        count = 0
        while userInput != "Hello":
            count += 1
            print("This is your " + str(count) + " wrong try.")
            userInput = input("Give me a string")
        print("Success!")

    inputFunc()