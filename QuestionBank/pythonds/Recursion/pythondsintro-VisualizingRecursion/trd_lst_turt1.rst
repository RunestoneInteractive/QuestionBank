.. activecode:: trd_lst_turt1
    :author: Majid Rouhani
    :difficulty: 0.0
    :basecourse: pythonds
    :chapter: Recursion
    :subchapter: pythondsintro-VisualizingRecursion
    :topics: Recursion/pythondsintro-VisualizingRecursion
    :from_source: F
    :caption: Drawing a Recursive Spriral using turtle. Correct the code to draw a recursive spiral
    :nocodelens:


    import turtle

    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()

    def drawSpiral(myTurtle, lineLen):
        if lineLen > 0:
            myTurtle.forward(lineLen)
            ...
    drawSpiral(myTurtle,100)
    myWin.exitonclick()