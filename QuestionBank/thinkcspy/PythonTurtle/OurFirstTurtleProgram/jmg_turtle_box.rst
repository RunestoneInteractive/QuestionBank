.. activecode:: jmg_turtle_box
    :author: Jean Griffin
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: OurFirstTurtleProgram
    :topics: PythonTurtle/OurFirstTurtleProgram
    :from_source: F
    :nocodelens:
    :hidecode:
    :autorun:

    import turtle               # This lets us use the turtle code 
    screen = turtle.Screen()    # Create a screen for drawing turtles
    pat = turtle.Turtle()       # Create a turtle named pat

    # Draw Side 1
    pat.forward(150)            # move forward 150 steps
    pat.left(90)                # turn left by 90 degrees

    # Draw Side 2
    pat.forward(150)            
    pat.left(90)    
              
    # Draw Side 3
    pat.forward(100)           # BUG 
    pat.left(90)    
            
    # Draw Side 4
    pat.forward(150)