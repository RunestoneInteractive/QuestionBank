.. activecode:: Function_Add_Var
  :author: bmiller
  :difficulty: 3.0
  :basecourse: TeacherCSP
  :chapter: CSPNameNames
  :subchapter: namesInput
  :topics: CSPNameNames/namesInput
  :from_source: T
  :tour_1: "Important lines tour"; 1-10: sqvar-line1-10; 2: sqvar-line2; 3: sqvar-line3; 4: sqvar-line4; 5-10: sqvar-line5-10; 12-14: sqvar-line12-14; 15: sqvar-line15;
  :nocodelens:

  def square(turtle):
      size = 50
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.right(90)

  from turtle import *  # use the turtle library
  space = Screen()      # create a turtle screen
  malik = Turtle()      # create a turtle named malik
  square(malik)         # draw a square with malik