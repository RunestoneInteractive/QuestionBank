.. activecode:: chmod_01
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: modules
    :topics: PythonModules/modules
    :from_source: T
    :nocodelens:

    import turtle            # allows us to use the turtles library

    wn = turtle.Screen()     # creates a graphics window
    alex = turtle.Turtle()   # create a turtle named alex

    alex.forward(150)        # tell alex to move forward by 150 units
    alex.left(90)            # turn by 90 degrees
    alex.forward(75)         # complete the second side of a rectangle
    wn.exitonclick()