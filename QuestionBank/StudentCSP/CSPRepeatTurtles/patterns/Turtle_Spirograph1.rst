.. activecode:: Turtle_Spirograph1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatTurtles
    :subchapter: patterns
    :topics: CSPRepeatTurtles/patterns
    :from_source: T
    :tour_1: "Lines of code"; 1-2: tr3-1-line1-2; 3: tr3-1-line3; 4: tr3-1-line4; 5: tr3-1-line5; 6: tr3-1-line6; 8: tr3-1-line8; 9: tr3-1-line9; 10: tr3-1-line10; 13: tr3-1-line13; 14: tr3-1-line14; 15: tr3-1-line15;
    :nocodelens:

    from turtle import *     # use the turtle library
    from sys import *        # use the system library
    setExecutionLimit(50000) # let this take up to 50 seconds
    space = Screen()         # create a turtle space
    zoe = Turtle()           # create a turtle named zoe
    zoe.setheading(90)       # point due north

    for repeats in range(20):   # draw the pattern 20 times
        zoe.forward(10)                 # Offset the shapes a bit
        zoe.right(18)                   # And turn each one a bit

        # This part makes a pentagon
        for sides in range(5):    # repeat 5 times
            zoe.forward(50)         # move forward by 50 unit
            zoe.right(72)           # turn by 72 degrees