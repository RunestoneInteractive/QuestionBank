.. activecode:: fnk
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: Functionscancallotherfunctions
    :topics: Functions/Functionscancallotherfunctions
    :from_source: None
    :nocodelens:

    import turtle

    def drawRectangle(t, w, h):
        """Get turtle t to draw a rectangle of width w and height h."""
        for i in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)

    def drawSquare(tx, sz):
        '''using drawRectangle to draw a square with sides sz long'''


    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.color('blue')
    drawRectangle(tess, 100, 50)
    tess.color('orange')

    wn.exitonclick()