.. activecode:: func_q17_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: T

    import turtle

    def drawSprite(t, numlegs, leglength):
       angle = 360/numlegs
       for i in range(numlegs):
          t.forward(leglength)
          t.backward(leglength)
          t.left(angle)

    def drawFancySquare(t, sz, lgs, lgl):
       for i in range(4):
           t.forward(sz)
           drawSprite(t, lgs, lgl)
           t.left(90)

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    drawFancySquare(alex, 100, 10, 15)

    wn.exitonclick()