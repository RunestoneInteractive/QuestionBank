.. activecode:: tgg
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: PythonTurtle
    :subchapter: IterationSimplifiesourTurtleProgram
    :topics: PythonTurtle/IterationSimplifiesourTurtleProgram
    :from_source: None
    :nocodelens:

    import turtle            # set up alex
    wn = turtle.Screen()
    alex = turtle.Turtle()

    for aColor in ["yellow", "red", "purple", "blue"]:
        alex.color(aColor)
        alex.forward(50)
        alex.left(90)

    wn.exitonclick()