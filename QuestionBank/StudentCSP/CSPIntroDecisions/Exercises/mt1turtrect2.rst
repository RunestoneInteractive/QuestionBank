.. parsonsprob:: mt1turtrect2
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: Exercises
   :topics: CSPIntroDecisions/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 

   Put the blocks in order to define a function draw_rect that draws a rectangle using 
   the passed turtle with its top left corner at (xpos, ypos) and with the given width 
   and height.  Before you move the turtle 
   make sure that it is heading east (0).
   -----
   def turtle_rect(turtle,xpos, ypos, width, height):
   =====
       turtle.setheading(0)
       turtle.penup()
   =====
       turtle.goto(xpos,ypos)
   =====
       turtle.goTo(xpos,ypos) #paired
   =====
       turtle.pendown()
   =====
       for i in range(2):
   =====
       for i in range(4): #paired
   =====
           turtle.forward(width)
   =====
           turtle.forward(100) #paired
   =====
           turtle.right(90)
   =====
           turtle.left(90) #paired
   =====
           turtle.forward(height)
           turtle.right(90)