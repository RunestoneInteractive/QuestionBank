.. activecode:: Turtle_Error2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameTurtles
    :subchapter: TurtlePractice
    :topics: CSPNameTurtles/TurtlePractice
    :from_source: T
    :nocodelens:

    from turtle Import *    # use the turtle library
    space = Screen()        # create a turtle space
    alex = Turtle           # create a turtle named alex
    alex.left(180)          # turn alex by 180 degrees
    alex.forward(75)        # move forward by 75 units
    alex.turn(90)           # turn left 90 degrees
    alex.forward(100)       # more forward by 100 units
    alex.left(90)           # turn left 90 degrees
    alex.forward            # move forward by 75 units