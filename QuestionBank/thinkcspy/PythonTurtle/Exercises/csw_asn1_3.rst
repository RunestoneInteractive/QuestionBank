.. activecode:: csw_asn1_3
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :caption: Asn 1-3
   :nocodelens:
   :language: python
   
   Complete the following program to use a turtle to draw five
   concentric circles. Your job is to write the body of the loop
   that draws the circles. For an additional challenge (but no extra
   credit) draw three bullseyes at different locations in the window.
   ~~~~
   '''
   Asn1-3.py: Draw five concentric circles
   Input:     None
   Output:    Concentric circles
   Author:
   '''
   import turtle

   wn = turtle.Screen()
   jan = turtle.Turtle()

   for r in range(10, 50, 10):
       #Put your code here

   wn.exitonclick()  #This should be your last statement