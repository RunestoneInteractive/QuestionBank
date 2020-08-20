.. activecode::  ch14ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPTurtleDecisions
    :subchapter: ch14_exercises
    :topics: CSPTurtleDecisions/ch14_exercises
    :from_source: T
    :nocodelens:

    from turtle import *             # use the turtle library
    from sys import *                # use the system library
    setExecutionLimit(100000)        # let this take up to 100 seconds
    space = Screen()                 # create a turtle screen (space)

    width = space.window_width()     # get the width of the screen (space)
    maxX = width / 2                 # set the max x value to half the width

    sue = Turtle()                   # create a turtle named sue
    sue.pensize(10)                  # set the pen width

    for y in range(10):              # repeat 10 times
        sue.penup()                      # pick up the pen
        if y % 5 == 0:
            sue.color('red')                 # set the color to red
        if y % 5 == 1:
            sue.color('black')
        if y % 5 == 2:
            sue.color('orange')
        if y % 5 == 3:
            sue.color('green')
        if y % 5 == 4:
            sue.color('blue')
        sue.goto(-1 * maxX,y * 10)       # move to the next row
        sue.pendown()                    # put the pen down
        sue.forward(width)               # move forward by the width