.. activecode::  ch14ex5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPTurtleDecisions
    :subchapter: ch14_exercises
    :topics: CSPTurtleDecisions/ch14_exercises
    :from_source: T
    :nocodelens:

    def turtleLoop(jaz, maxX):
        for x in range(10):       # repeat the body 10 times
            jaz.forward(100)           # go forward 100
            jaz.right(120)             # turn right 120 degrees
            jaz.forward(100)           # go forward 100
            jaz.left(120)              # turn left 120 degrees
            if (jaz.xcor() >= maxX):   # if at right edge of space
                jaz.penup()                # pick up the pen
                jaz.goto(-1 * maxX,jaz.ycor() - 100)  # move left & down
                jaz.pendown()              # put the pen down

    def turtleProcedure(width, jaz):
        space.setup(width,width)  # set the space width and height
        maxX = width / 2          # set the max x value to half the width
        jaz.shape('turtle')       # set the shape for jaz to turtle
        jaz.penup()               # pick up the pen (don't draw)
        jaz.goto(-1 * maxX,100)   # go to the left side of the space
        jaz.pendown()             # put the pen down to draw with
        jaz.left(60)              # turn the turtle left 60 degrees
        turtleLoop(jaz, maxX)     # call the other function


    from turtle import *      # use the turtle library
    from sys import *         # use the system library
    setExecutionLimit(50000)  # let this take up to 50 seconds
    space = Screen()          # create a turtle screen (space)

    width = 400               # set the desired width
    jaz = Turtle()            # create a turtle named jaz
    turtleProcedure(width,jaz)