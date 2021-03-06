.. mchoice:: test_question3_1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: OurFirstTurtleProgram
   :topics: PythonTurtle/OurFirstTurtleProgram
   :from_source: T
   :practice: T
   :answer_a: It creates a new turtle object that can be used for drawing.
   :answer_b: It defines the module turtle which will allow you to create a Turtle object and draw with it.
   :answer_c: It makes the turtle draw half of a rectangle on the screen.
   :answer_d: Nothing, it is unnecessary.
   :correct: b
   :feedback_a: The line &quotalex = turtle.Turtle()&quot is what actually creates the turtle object.
   :feedback_b: This line imports the module called turtle, which has all the built in functions for drawing on the screen with the Turtle object.
   :feedback_c: This functionality is performed with the lines: &quotalex.forward(150)&quot, &quotlex.left(90)&quot, and &quotalex.forward(75)&quot
   :feedback_d: If we leave it out, Python will give an error saying that it does not know about the name &quotturtle&quot when it reaches the line &quotwn = turtle.Screen()&quot
   :pct_on_first: 0.672143676
   :total_students_attempting: 18319
   :num_students_correct: 18261.0
   :mean_clicks_to_correct: 1.3938995674

   Consider the following code:
   
   .. code-block:: python
   
     import turtle
     wn = turtle.Screen()
     alex = turtle.Turtle()
     alex.forward(150)
     alex.left(90)
     alex.forward(75)
   
   What does the line "import turtle" do?