.. mchoice:: question3_2_2_cofi_Q5_lad
   :author: Lynda Danielson
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: OurFirstTurtleProgram
   :topics: PythonTurtle/OurFirstTurtleProgram
   :from_source: F
   :answer_a: It creates a new turtle object that can be used for drawing.
   :answer_b: It makes the turtle draw a line of length 90.
   :answer_c: It makes the turtle draw half of a rectangle on the screen.
   :answer_d: It turns the turtle toward the north.
   :correct: d
   :feedback_a: The line &quotalex = turtle.Turtle()&quot is what actually creates the turtle object.
   :feedback_b: Recall that the .forward() method would draw a line.
   :feedback_c: This functionality is performed with the lines: &quotalex.forward(150)&quot, &quotlex.left(90)&quot, and &quotalex.forward(75)&quot
   :feedback_d: This is correct since the turtle is initially facing east and when turned left 90 degrees it will be facing north.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Consider the following code:
   
   .. code-block:: python
   
     import turtle
     wn = turtle.Screen()
     alex = turtle.Turtle()
     alex.forward(150)
     alex.left(90)
     alex.forward(75)
   
   What does the line "alex.left(90)" do?