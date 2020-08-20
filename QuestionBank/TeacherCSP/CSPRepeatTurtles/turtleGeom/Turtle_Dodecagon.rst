.. activecode:: Turtle_Dodecagon
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: turtleGeom
    :topics: CSPRepeatTurtles/turtleGeom
    :from_source: T
    :tour_1: "Lines of code"; 1: tR3-line1; 2: tR3-line2; 3: tR5-line3; 4: tR5-line4; 5: tR5-line5; 6: tR5-line6; 7: tR5-line7;
    :nocodelens:

    from turtle import *        # use the turtle library
    space = Screen()            # create a turtle space
    mia = Turtle()              # create a turtle named maria
    mia.setheading(90)          # point due north
    for sides in range(12):     # repeat the indented lines 12 times
        mia.forward(40)         # move forward by 40 units
        mia.right(??)           # change ?? to the amount to turn