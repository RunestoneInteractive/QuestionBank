.. mchoice:: question 2
    :author: David Birrow
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Debugging
    :subchapter: Exercises
    :topics: Debugging/Exercises
    :from_source: F
    :answer_a: Syntax
    :answer_b: Type
    :answer_c: Name
    :answer_d: No error
    :correct: c
    :feedback_a: No syntax error.
    :feedback_b: Not a type error
    :feedback_c: Yes, there are two capital "T's" in the line that initialized alex the turtle
    :feedback_d: There's definitely an error

    This code looks correct, but something is up. What type of error is it? 

    import turtle

    wn = turtle.Screen()    
         
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()          

    tess.color("hotpink")

    tess.pensize(5)

    alex = Turtle.Turtle()           

    tess.forward(80)
                 
    tess.left(120)

    tess.forward(80)

    tess.left(120)   
                
    wn.exitonclick()