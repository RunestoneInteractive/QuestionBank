.. activecode:: CS152_Function_Shape_Practice
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: functions
    :topics: Functions/functions
    :from_source: F
    :nocodelens:

    Write a program to

    a) Draw a row of 3 squares by calling drawSquare in a loop

    b) Write a function drawTriangle. Mimic what is done in drawSquare.

    c) Draw row of 5 triangles by calling drawTriangle in a loop

    d) Write a function drawHexagon. Mimice what is done in drawSquare.

    e) Draw a row of 4 hexagons by calling drawHexagon in a loop

    If you finish this,

    a) Write a function drawPoly(t, sz, sides) where sides is the number of sides in the shape

    b) Keep your main program the same but rewrite your other functions to call drawPoly

    ~~~~
    import turtle

    def drawSquare(t, sz):
        """Make turtle t draw a square of with side sz."""
        for i in range(4):
            t.forward(sz)
            t.left(90)

    wn = turtle.Screen()              # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()            # create alex
    drawSquare(alex, 50)             # Call the function to draw the square passing the actual turtle and the actual side size

    wn.exitonclick()