.. activecode::  ch14ex7q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: studentcsp
     :chapter: CSPTurtleDecisions
     :subchapter: Exercises
     :topics: CSPTurtleDecisions/Exercises
     :from_source: T
     :nocodelens:

     from turtle import *      # use the turtle library
     import random
     space = Screen()          # create a turtle screen (space)
     width = space.window_width()
     height = space.window_height()
     maxX = width / 2  # get the max x value
     minX = -1 * maxX
     maxY = height / 2
     minY = -1 * maxY
     jaz = Turtle()            # create a turtle named jaz
     for num in range(10):
         if num % 2 == 0              # if even row
             jaz.color('red')          # set the color to red
         if num % 2 == 1:             # if odd row
         jaz.color('black')       # set the color to black
         randX = random.randrange(minX, maxX)
         randY = random.randrange(minY, maxY)
         jaz.goto(randX,randY)