.. activecode::  ch14ex2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPTurtleDecisions
    :subchapter: Exercises
    :topics: CSPTurtleDecisions/Exercises
    :from_source: T
    :nocodelens:

    def draw(jaz, maxX):
        for x in range(3):
            jaz.forward(100)
            jaz.right(120)
            jaz.forward(100)
            jaz.left(120)
            if (jaz.xcor() <= maxX):
                jaz.penup()
                jaz.goto(-1 * maxX,jaz.ycor() - 100)
                jaz.pendown()

    def turtleSetup(width, jaz):
        space.setup(width,width)  # set the space width and height
        maxX = width / 2          # set the max x value to half the width
        jaz.shape('turtle')
        jaz.penup()
        jaz.goto(-1 * maxX,100)
        jaz.pendown()
        jaz.left(60)
        draw(jaz, maxX)


    from turtle import *      # use the turtle library
    from sys import *         # use the system library
    setExecutionLimit(50000)  # let this take up to 50 seconds
    space = Screen()          # create a turtle screen (space)
    jaz = Turtle()
    width = 400

    turtleSetup(width, jaz)