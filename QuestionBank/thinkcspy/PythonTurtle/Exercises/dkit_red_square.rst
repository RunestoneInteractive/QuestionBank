.. activecode:: dkit_red_square
    :author: Jean Griffin
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :nocodelens:
    :hidecode:
    :autorun:
    :caption: SHOW CODE -- FIX 2 BUGS -- SAVE & RUN --

    This program is supposed to draw a red square but it has 2 bugs.
    To fix them, 1) Show Code. 2) FIX THE BUG(s). 3) Save & Run
    ~~~~
    # START SETUP
    import turtle             # Bring in the turtle code 
    screen = turtle.Screen()  # Create a screen for drawing
    pat = turtle.Turtle()     # Create a turtle named pat
    # END SETUP

    pat.color("green")        # FIX THE BUG

    # Draw Side 1
    pat.forward(150)          # move forward 150 steps
    pat.left(90)              # turn left by 90 degrees

    # Draw Side 2
    pat.forward(150)            
    pat.left(90)    
              
    # Draw Side 3
    pat.forward(100)          # FIX THE BUG        
    pat.left(90)    
            
    # Draw Side 4
    pat.forward(150)