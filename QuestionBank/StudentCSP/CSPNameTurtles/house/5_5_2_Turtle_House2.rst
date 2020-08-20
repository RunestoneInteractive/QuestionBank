.. parsonsprob:: 5_5_2_Turtle_House2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: house
   :topics: CSPNameTurtles/house
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.7405660377
   :total_students_attempting: 848
   :num_students_correct: 783.0
   :mean_clicks_to_correct: 1.4572158365

   Align the program pieces below to make the house and window figure above.  Draw the square first for the main part of the house, next draw the roof, and finally draw the window.
   -----
   from turtle import *
   space = Screen()
   bob = Turtle()
   =====
   from turtle import *
   space = screen()
   bob = turtle() #paired
   =====
   # Make a square
   bob.forward(100)
   bob.right(90)
   bob.forward(100)
   bob.right(90)
   bob.forward(100)
   bob.right(90)
   bob.forward(100)
   =====
   # Position for roof
   bob.right(90)
   =====
   # Position for roof
   bob.left(90) #paired
   =====
   # Make a roof
   bob.forward(100)
   bob.right(-120)
   bob.forward(100)
   bob.right(-120)
   bob.forward(100)
   bob.right(-120)
   =====
   # Position for window
   bob.penup()
   bob.goto(50,-30)
   bob.pendown()
   bob.setheading(0)
   =====
   # Draw window
   bob.color("red")
   bob.forward(30)
   bob.right(90)
   bob.forward(30)
   bob.right(90)
   bob.forward(30)
   bob.right(90)
   bob.forward(30)