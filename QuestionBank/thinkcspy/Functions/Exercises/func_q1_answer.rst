.. activecode:: func_q1_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: T

    import turtle

    def drawSquare(t, sz):
        """Make turtle t draw a square of with side sz."""
        for i in range(4):
            t.forward(sz)
            t.left(90)

    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()     # create alex
    alex.color('hotpink')
    alex.pensize(3)

    for i in range(5):
        drawSquare(alex, 20)   # Call the function to draw the square
        alex.penup()
        alex.forward(40)       # move alex to the starting position for the next square
        alex.pendown()

    wn.exitonclick()