.. activecode::  ch10ex5q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPRepeatTurtles
     :subchapter: Exercises
     :topics: CSPRepeatTurtles/Exercises
     :from_source: T
     :nocodelens:

     from turtle import *    # use the turtle library
     space = Screen()        # create a turtle space
     will = Turtle()                 # create a turtle named will
     will.setheading(90)     # point due north
     for sides in range(x):  # repeat the indented lines
         will.forward(100)           # move forward by 100 units
         will.right(y)