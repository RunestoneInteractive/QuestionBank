.. activecode:: cturtle_practical_example_Python
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: pattern_application
    :topics: Turtles/pattern_application
    :from_source: T
    :language: Python

    import turtle

    SQUARE_SIZE = 35

    wn = turtle.Screen()
    wn.tracer(0);
    square = turtle.Turtle()
    square.speed(10)
    square.pu()
    square.goto(-turtle.window_width()/2,turtle.window_height()/2);
    square.pd()

    a = 0
    b = 0
    for i in range(8):
        if(b == 0):
            a=1
        else:
            a=0
        for j in range(8):
            square.penup()
            square.goto(-turtle.window_width() / 2 + j * SQUARE_SIZE, (-turtle.window_height() / 2) + i * SQUARE_SIZE + SQUARE_SIZE)
            square.pendown()
            if(a==0):
                square.fillcolor('orange')
                a=1
            else:
                square.fillcolor('blue')
                a=0
            square.begin_fill()
            for k in range(4):
                square.forward(SQUARE_SIZE)
                square.right(90)
            square.end_fill()
        if(b==0):
            b=1
        else:
            b=0
    wn.tracer(1)