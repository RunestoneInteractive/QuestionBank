.. activecode:: tgl
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: PythonTurtle
   :subchapter: AFewMoreturtleMethodsandObservations
   :topics: PythonTurtle/AFewMoreturtleMethodsandObservations
   :from_source: None
   :nocodelens:

   import turtle
   wn = turtle.Screen()
   wn.bgcolor("lightgreen")
   tess = turtle.Turtle()
   tess.color("blue")
   tess.shape("turtle")

   print(list(range(5, 84, 2)))
   tess.up()                       # this is new
   for size in range(5, 84, 2):    # start with size = 5 and grow by 2

       tess.forward(size)          # move tess along
       tess.right(24)              # and turn her

   wn.exitonclick()