.. activecode:: lab0401aa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: lab04_01a
    :topics: Labs/lab04_01a
    :from_source: T
    :nocodelens:

    import turtle

    def drawPolygon(t, sideLength, numSides):
        turnAngle = 360 / numSides
        for i in range(numSides):
            t.forward(sideLength)
            t.right(turnAngle)

    def drawCircle(anyTurtle, radius):
        circumference = 2 * 3.1415 * radius
        sideLength = circumference / 360
        drawPolygon(anyTurtle, sideLength, 360)


    wn = turtle.Screen()
    wheel = turtle.Turtle()

    drawCircle(wheel, 20)

    wn.exitonclick()