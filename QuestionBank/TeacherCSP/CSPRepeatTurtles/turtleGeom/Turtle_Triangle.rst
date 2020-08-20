.. activecode:: Turtle_Triangle
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: turtleGeom
    :topics: CSPRepeatTurtles/turtleGeom
    :from_source: T
    :tour_1: "Lines of code"; 1: tR3-line1; 2: tR3-line2; 3: tR3-line3; 4: tR3-line4; 5: tR3-line5; 6: tR3-line6; 7: tR3-line7;
    :nocodelens:

    from turtle import *        # use the turtle library
    space = Screen()            # create a turtle space
    avery = Turtle()            # create a turtle named avery
    avery.setheading(90)        # point due north
    for sides in range(3):      # repeat the indented lines 3 times
        avery.forward(100)      # move forward by 100 units
        avery.right(120)                # turn by 120 degrees