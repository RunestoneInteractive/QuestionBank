.. activecode:: Turtle_Nested_Error1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatTurtles
    :subchapter: patterns
    :topics: CSPRepeatTurtles/patterns
    :from_source: T
    :nocodelens:

    from turtle import *    # use the turtle library
    from sys import *
    setExecutionLimit(50000)

    wn = Screen
    mateo = Turtle()
    mateo.setheading(90)

    for repeats in range(20)
        mateo.color("red")
        mateo.forward(10)
        mateo.left(18)

        for sides in range(3):
            mateo.Color("blue")
            mateo.forward(50)
            mateo.Right(120)