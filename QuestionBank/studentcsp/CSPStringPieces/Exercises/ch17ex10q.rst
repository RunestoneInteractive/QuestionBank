.. activecode::  ch17ex10q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPStringPieces
    :subchapter: Exercises
    :topics: CSPStringPieces/Exercises
    :from_source: T
    :nocodelens:

    def witchStory (input):

        # split at the comma
        pieces = input.split(",")

        # initialize the variables
        firstName = pieces[0]
        lastName = pieces[1]
        gender = pieces[2]
        address = pieces[3]
        verb = pieces[4]

        # create the story
        start = "Once there was a " + gender + " named " + firstName + "."
        next1 = "A good " + gender + " living at " + address + "."
        next2 = "One day, a wicked witch came to the " + lastName + " house."
        next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
        ending = "But " + firstName + " was smart and avoided the wicked witch."

        # print the story
        print(start)
        print(next1)
        print(next2)
        print(next3)
        print(ending)

    # call the procedure
    witchStory("Abe,Brown,boy,1313 Maple Lane,trick")