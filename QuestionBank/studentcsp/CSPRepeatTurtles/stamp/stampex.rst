.. activecode:: stampex
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPRepeatTurtles
   :subchapter: stamp
   :topics: CSPRepeatTurtles/stamp
   :from_source: T
   :tour_1: "Line-by-line Tour"; 1: stamp1-line1; 2: stamp1-line2; 3: stamp1-line3; 4: stamp1-line4; 5: stamp1-line5; 7: stamp1-line7; 8: stamp1-line8; 9: stamp1-line9; 10: stamp1-line10; 11: stamp1-line11; 12: stamp1-line12;
   :nocodelens:

   from turtle import *
   space = Screen()
   tess = Turtle()
   tess.color("blue")
   tess.shape("turtle")

   print(range(5, 60, 2))
   tess.penup()                  # ask tess to pick up her pen
   for size in range(5, 60, 2):  # start with size = 5 and grow by 2
       tess.stamp()                # leave an impression on the canvas
       tess.forward(size)          # move tess along
       tess.right(24)              # and turn her