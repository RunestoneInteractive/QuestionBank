.. actex:: CS152_Range_Practice_2
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F

    Copy your working program from the previous exercise, then

       #.  Have the user input the number of steps from 1 to 10, and use that value as the range parameter.
       #.  Make the length/height of a step proportional to the number of steps. The more steps, the smaller each one is.

    ~~~~
    import turtle
    wn = turtle.Screen()
    jess = turtle.Turtle()
    jess.forward(30)
    jess.left(90)
    jess.forward(30)
    jess.right(90)