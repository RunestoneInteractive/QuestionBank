.. activecode:: Turtle_House
  :author: bmiller
  :difficulty: 3.0
  :basecourse: TeacherCSP
  :chapter: CSPNameTurtles
  :subchapter: house
  :topics: CSPNameTurtles/house
  :from_source: T
  :tour_1: "Section Tour"; 1-3: house-line1-3; 6-12: house-line5-11; 15: house-line13; 18-23: house-line18-23;
  :nocodelens:

  from turtle import *      # use the turtle library
  space = Screen()          # create a turtle screen (space)
  bob = Turtle()            # create a turtle named bob

  # Make a square
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(90)             # turn right by 90 degrees
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(90)             # turn right by 90 degrees
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(90)             # turn right by 90 degrees
  bob.forward(100)          # tell bob to move forward by 100 units

  # Position for roof
  bob.right(90)

  # Make a roof
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(-120)           # turn LEFT by 120 degrees
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(-120)           # turn LEFT by 120 degrees
  bob.forward(100)          # tell bob to move forward by 100 units
  bob.right(-120)           # turn LEFT by 120 degrees