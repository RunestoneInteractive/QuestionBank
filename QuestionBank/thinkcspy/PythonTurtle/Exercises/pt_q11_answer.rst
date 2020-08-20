.. activecode:: pt_q11_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: T
    :nocodelens:

    import turtle

    tanenbaum = turtle.Turtle()

    tanenbaum.hideturtle()
    tanenbaum.speed(20)

    for i in range(350):
        tanenbaum.forward(i)
        tanenbaum.right(98)