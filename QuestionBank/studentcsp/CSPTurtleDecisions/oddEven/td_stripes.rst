.. activecode:: td_stripes
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPTurtleDecisions
    :subchapter: oddEven
    :topics: CSPTurtleDecisions/oddEven
    :from_source: T
    :tour_1: "Structural Tour"; 1-4: td2a-line1-4; 6-7: td2a-line6-7; 9-10: td2a-line9-10; 12: td2a-line12; 13: td2a-line13; 14-15: td2a-line14-15; 16-17: td2a-line16-17; 18: td2a-line18; 19: td2a-line19; 20: td2a-line20;
    :nocodelens:

    from turtle import *             # use the turtle library
    from sys import *                # use the system library
    setExecutionLimit(100000)        # let this take up to 100 seconds
    space = Screen()                 # create a turtle screen (space)

    width = space.window_width()     # get the width of the screen (space)
    maxX = width / 2                 # set the max x value to half the width

    sue = Turtle()                   # create a turtle named sue
    sue.pensize(10)                  # set the pen width

    for y in range(5):               # repeat 5 times
        sue.penup()                      # pick up the pen
        if y % 2 == 0:                   # if even row
            sue.color('red')                 # set the color to red
        if y % 2 == 1:                   # if odd row
            sue.color('black')               # set the color to black
        sue.goto(-1 * maxX,y * 10)       # move to the next row
        sue.pendown()                    # put the pen down
        sue.forward(width)               # move forward by the width