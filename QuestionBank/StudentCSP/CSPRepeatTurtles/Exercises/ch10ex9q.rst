.. activecode::  ch10ex9q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPRepeatTurtles
     :subchapter: Exercises
     :topics: CSPRepeatTurtles/Exercises
     :from_source: T
     :nocodelens:

     from turtle import *     # use the turtle library
     from sys import *        # use the system library
     setExecutionLimit(50000) # let this take up to 50 seconds
     space = Screen()         # create a turtle space
     zoe = Turtle()           # create a turtle named zoe
     zoe.setheading(90)       # point due north

     for repeats in range(20):   # draw the pattern 20 times
         zoe.forward(10)             # Offset the shapes a bit
         zoe.right(18)               # And turn each one a bit

     # This part makes a pentagon
     for sides in range(5):    # repeat 5 times
         zoe.forward(50)         # move forward by 50 unit
         zoe.right(72)           # turn by 72 degrees