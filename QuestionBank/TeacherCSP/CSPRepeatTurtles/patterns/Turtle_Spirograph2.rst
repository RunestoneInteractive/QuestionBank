.. activecode:: Turtle_Spirograph2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: patterns
    :topics: CSPRepeatTurtles/patterns
    :from_source: T
    :tour_1: "Lines of code"; 1-2: tr3-1-line1-2; 3: tr3-1-line3; 4: tr3-1-line4; 5: tr3-1-line5; 6: tr3-1-line6; 8: tr3-1-line8; 9: ts2-line9; 10: ts2-line10; 11: ts2-line11; 12: ts2-line12; 15: ts2-line15; 16: ts2-line16; 17: ts2-line17;
    :nocodelens:

    from turtle import *     # use the turtle library
    from sys import *        # use the system library
    setExecutionLimit(50000) # let this take up to 50 seconds
    space = Screen()         # create a turtle space
    zoe = Turtle()           # create a turtle named zoe
    zoe.setheading(90)       # point zoe due north

    for repeats in range(20):   # 20 times to draw the pattern
        zoe.color("green")      # set the color to green
        zoe.forward(10)           # Offset the shapes a bit
        zoe.right(18)             # And turn each one a bit
        zoe.color("red")          # set the color to red

        # This part makes a pentagon
        for sides in range(5):    # repeat 5 times
            zoe.forward(50)         # move forward 50 units
            zoe.right(72)           # turn by 72 degrees