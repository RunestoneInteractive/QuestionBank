.. activecode::  ch14ex4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPTurtleDecisions
    :subchapter: Exercises
    :topics: CSPTurtleDecisions/Exercises
    :from_source: T
    :nocodelens:

    from turtle import *      # use the turtle library
    from sys import *         # use the system library
    setExecutionLimit(50000)  # let this take up to 50 seconds
    space = Screen()          # create a turtle screen (space)

    height = 400               # set the desired height
    space.setup(height,height)  # set the space width and height
    maxY = height / 2          # set the max y value to half the height
    t = Turtle()
    t.shape('turtle')

    for x in range(10):
    if (100 + t.ycor() > maxY):
    t.color("blue")
    t.left(180)
    t.backward(100)
    elif (t.ycor() - 100 > (-1* maxY)):
    t.color("red")
    t.left(180)
    t.forward(100)
    else
    t.color("green")
    t.forward(100)