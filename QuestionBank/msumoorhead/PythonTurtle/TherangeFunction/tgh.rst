.. activecode:: tgh
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: PythonTurtle
   :subchapter: TherangeFunction
   :topics: PythonTurtle/TherangeFunction
   :from_source: None
   :nocodelens:

   import turtle            # set up alex
   wn = turtle.Screen()
   alex = turtle.Turtle()

   for i in range(4):
       alex.forward(50)
       alex.left(90)

   wn.exitonclick()