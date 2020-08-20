.. activecode:: tge
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: PythonTurtle
   :subchapter: IterationSimplifiesourTurtleProgram
   :topics: PythonTurtle/IterationSimplifiesourTurtleProgram
   :from_source: None
   :nocodelens:

   import turtle            # set up alex
   wn = turtle.Screen()
   alex = turtle.Turtle()

   for aSide in [0, 1, 2, 3]:      # four items in list
       alex.forward(50)
       alex.left(90)

   wn.exitonclick()