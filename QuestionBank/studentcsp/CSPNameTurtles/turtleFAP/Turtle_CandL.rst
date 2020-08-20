.. activecode:: Turtle_CandL
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPNameTurtles
    :subchapter: turtleFAP
    :topics: CSPNameTurtles/turtleFAP
    :from_source: T
    :nocodelens:

    from turtle import *  # use the turtle library
    space = Screen()      # create a turtle space
    ji = Turtle()         # create a turtle named ji
    ji.right(180)         # turn right by 180 degrees
    ji.forward(75)        # move forward by 75 units
    ji.right(90)          # turn right 90 degrees
    ji.forward(100)       # more forward by 90 units
    ji.right(90)          # turn right 90 degrees
    ji.forward(75)        # move forward by 75 units
    ji.penup()            # pick up the pen
    ji.forward(50)        # move forward 50 units
    ji.pendown()          # put the pen down
    ji.right(90)          # turn right 90 degrees
    ji.forward(100)       # go forward 100 units
    ji.left(90)           # turn left 90 degrees
    ji.forward(75)        # go forward 75 units