.. activecode:: Turtles_Voorbeeld2
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python

    
    ~~~~
    import turtle               
    wn = turtle.Screen()  
    wn.bgcolor("lightgreen")      
    alex = turtle.Turtle()    
    alex.color("blue")
    alex.pensize(3)
    alex.speed(10)
    alex.forward(150)           
    alex.left(90)               
    alex.forward(75)