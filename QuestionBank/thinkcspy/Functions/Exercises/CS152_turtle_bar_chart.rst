.. actex:: CS152_turtle_bar_chart
    :author: John Cigas
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F

    There was a whole program in :ref:`bar_chart` to create a bar chart with specific data.  Creating a bar chart is a useful idea in general.  Modify the program below to

    1. Write a non-fruitful function called barChart, that takes the numeric list of data as a parameter, and draws the bar chart.  

    2. Modify the current version of the ``drawBar`` function. The current version unfortunately draws the top of the bar through the bottom of the label.  A nice elaboration is to make the label appear completely above the top line.  The fill action makes this modification particularly tricky:  You will want to move past the top of the bar and write before or after drawing and filling the bar. You will find that you already have written a function that helps with this. You should copy that function to this program and use it!

    3. Make your program even more flexible by passing an extra parameter to ``drawBar`` for the distance to move up.  For the ``barChart`` function make that parameter be some small fraction of ``maxheight+border``.  
    ~~~~

    import turtle

    def drawBar(t, height):
        """ Get turtle t to draw one bar, of height. """
        t.begin_fill()               # start filling this shape
        t.left(90)
        t.forward(height)
        t.write(str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()                 # stop filling this shape


    def main():
        xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
        maxheight = max(xs)
        numbars = len(xs)
        border = 10

        wn = turtle.Screen()             # Set up the window and its attributes
        wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
        wn.bgcolor("lightgreen")

        tess = turtle.Turtle()           # create tess and set some attributes
        tess.color("blue")
        tess.fillcolor("red")
        tess.pensize(3)

        for a in xs:
            drawBar(tess, a)

        wn.exitonclick()

    main()