.. activecode:: Turtle_Names5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPNameTurtles
    :subchapter: changeProg
    :topics: CSPNameTurtles/changeProg
    :from_source: T
    :nocodelens:

    from turtle import *        # use the turtle library
    space = Screen()            # create a turtle screen (space)
    alex = Turtle()             # create a turtle named alex
    alex.forward(40)            # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
    alex.forward(40)            # complete the second leg of a triangle
    alex.left(0)                # ZERO won't actually work
    alex.forward(57)            # Close the triangle