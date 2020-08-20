.. activecode::  ch6ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPNameNames
     :subchapter: Exercises
     :topics: CSPNameNames/Exercises
     :from_source: T
     :nocodelens:

     def square(turtle,size):
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)


     from turtle import *    # use the turtle library
     space = Screen()        # create a turtle screen (space)
     malik = Turtle()        # create a turtle named malik
     square(100, malik)      # draw a square of size 100
     square(malik)               # draw a square of size 75
     square(50)          # draw a square of size 50
     square(malik, 25)       # draw a square of size 25