.. activecode:: ch17ex1a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    # initialize the variables
    firstName = "Pat"
    lastName = "Smith"
    gender = "girl"
    address = "65 Elm Street"
    verb = "eat"

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
    print (next3)
    print(ending)