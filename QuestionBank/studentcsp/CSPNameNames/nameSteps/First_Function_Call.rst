.. activecode:: First_Function_Call
  :author: bmiller
  :difficulty: 3.0
  :basecourse: studentcsp
  :chapter: CSPNameNames
  :subchapter: nameSteps
  :topics: CSPNameNames/nameSteps
  :from_source: T
  :tour_1: "Important lines tour"; 1-9: dsq2-line1-9; 11-13: dsq2-line11-13; 14: dsq2-line14;
  :nocodelens:

  def square(turtle):
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)

  from turtle import *  # use the turtle library
  space = Screen()      # create a turtle screen
  malik = Turtle()      # create a turtle named malik
  square(malik)         # draw a square with malik