.. actex:: CS152_Range_Practice_1
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F

    The program below draws one step in a staircase. 
    Modify it to 

       #.  Use variables to represent the values 30 and 90. Pick appropriate names.
       #.  Use a for loop to draw 5 steps, going up to the right.

    ~~~~
    import turtle
    wn = turtle.Screen()
    jess = turtle.Turtle()
    jess.forward(30)
    jess.left(90)
    jess.forward(30)
    jess.right(90)