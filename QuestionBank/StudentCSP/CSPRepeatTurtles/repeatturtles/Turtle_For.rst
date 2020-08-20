.. activecode:: Turtle_For
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatTurtles
    :subchapter: repeatturtles
    :topics: CSPRepeatTurtles/repeatturtles
    :from_source: T
    :tour_1: "Lines of code"; 1: tR1-line1; 2: tR1-line2; 3: tR1-line3; 4: tR1-line4; 5: tR1-line5; 6: tR1-line6; 7: tR1-line7;
    :nocodelens:

    from turtle import *        # use the turtle library
    space = Screen()            # create a turtle space
    alisha = Turtle()           # create a turtle named alisha
    alisha.setheading(90)       # point due north
    for sides in [1,2,3,4]:     # repeat the indented lines 4 times
        alisha.forward(100)             # move forward by 100 units
        alisha.right(90)                # turn by 90 degrees