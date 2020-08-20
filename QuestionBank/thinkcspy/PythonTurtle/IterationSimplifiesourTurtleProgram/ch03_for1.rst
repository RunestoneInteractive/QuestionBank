.. activecode:: ch03_for1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: IterationSimplifiesourTurtleProgram
   :topics: PythonTurtle/IterationSimplifiesourTurtleProgram
   :from_source: T
   :nocodelens:

   import turtle            # set up alex
   wn = turtle.Screen()
   alex = turtle.Turtle()

   for i in [0, 1, 2, 3]:      # repeat four times
       alex.forward(50)
       alex.left(90)

   wn.exitonclick()