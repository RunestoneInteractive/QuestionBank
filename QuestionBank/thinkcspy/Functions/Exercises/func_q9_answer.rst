.. activecode:: func_q9_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: T

    import turtle

    def drawFivePointStar(t):
        for i in range(5):
            t.forward(100)
            t.left(216)

    wolfram = turtle.Turtle()
    drawFivePointStar(wolfram)