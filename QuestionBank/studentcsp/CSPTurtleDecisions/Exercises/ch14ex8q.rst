.. activecode::  ch14ex8q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPTurtleDecisions
    :subchapter: Exercises
    :topics: CSPTurtleDecisions/Exercises
    :from_source: T
    :nocodelens:

    from turtle import *             # use the turtle library
    from sys import *                # use the system library
    setExecutionLimit(100000)        # let this take up to 100 seconds
    space = Screen()                 # create a turtle screen (space)

    height = space.window_height()     # get the height of the screen (space)
    width = space.window_width        #get the width
    maxY = height / 2                 # set the max y value to half the height
    maxX = width

    sue = Turtle()                   # create a turtle named sue
    sue.pensize(10)                  # set the pen width

    for x in range(4):               # repeat 5 times
        sue.penup()                      # pick up the pen
        if x % 2 == 0:                   # if even row
        sue.color('yellow')                 # set the color to yellow
        sue.goto(-1 * maxX, x * 10)
        sue.penup()
        sue.forward(height)
        sue.left(90)
        if x % 2 == 1:                   # if odd row
            sue.color('black')               # set the color to black
            sue.goto(x * 10,-1 * maxY)
            sue.pendown()
            sue.forward(height)
            sue.left(90)