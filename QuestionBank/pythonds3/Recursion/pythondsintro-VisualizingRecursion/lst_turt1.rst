.. activecode:: lst_turt1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: pythondsintro-VisualizingRecursion
    :topics: Recursion/pythondsintro-VisualizingRecursion
    :from_source: T
    :caption: Drawing a Recursive Spriral using turtle
    :nocodelens:


    import turtle


    def draw_spiral(my_turtle, line_len):
        if line_len > 0:
            my_turtle.forward(line_len)
            my_turtle.right(90)
            draw_spiral(my_turtle, line_len - 5)


    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()