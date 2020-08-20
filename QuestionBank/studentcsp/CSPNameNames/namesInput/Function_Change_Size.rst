.. activecode:: Function_Change_Size
  :author: bmiller
  :difficulty: 3.0
  :basecourse: studentcsp
  :chapter: CSPNameNames
  :subchapter: namesInput
  :topics: CSPNameNames/namesInput
  :from_source: T
  :tour_1: "Important lines tour"; 1-9: sq50-line1-9; 2,4,6,8: sq50-line2468; 11-13: sq50-line11-13; 14: sq50-line14;
  :nocodelens:

  def square(turtle):
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(50)
      turtle.right(90)

  from turtle import *  # use the turtle library
  space = Screen()      # create a turtle screen
  malik = Turtle()      # create a turtle named malik
  square(malik)         # draw a square with malik