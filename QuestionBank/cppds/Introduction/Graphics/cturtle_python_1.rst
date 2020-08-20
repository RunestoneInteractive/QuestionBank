.. activecode:: cturtle_python_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: Graphics
    :topics: Introduction/Graphics
    :from_source: T
    :optional:

    import turtle

    turt = turtle.Turtle()
    turt.fillcolor("purple")
    turt.speed("slowest")

    turt.begin_fill()
    for i in range(4):
        turt.forward(50)
        turt.right(90)
    turt.end_fill()
    turt.bye()