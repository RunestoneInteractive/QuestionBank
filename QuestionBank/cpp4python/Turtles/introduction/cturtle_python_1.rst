.. activecode:: cturtle_python_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: introduction
    :topics: Turtles/introduction
    :from_source: T
    :language: python

    import turtle

    turt = turtle.Turtle()
    turt.fillcolor("purple")
    turt.speed("slowest")

    turt.begin_fill()
    for i in range(4):
        turt.forward(50)
        turt.right(90)
    turt.end_fill()