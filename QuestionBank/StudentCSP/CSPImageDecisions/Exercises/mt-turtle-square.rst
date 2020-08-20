.. parsonsprob:: mt-turtle-square
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPImageDecisions
   :subchapter: Exercises
   :topics: CSPImageDecisions/Exercises
   :from_source: F
   :numbered: left

   Complete the turtle_square function that takes a turtle, xpos, ypos, and width and draws a square with the lower right corner at (xpos, ypos).  
   -----
   def turtle_square(turtle, xpos, ypos, width):
   =====
       turtle.setheading(90) 
       turtle.penup()
   =====
       turtle.goto(xpos,ypos)
   =====
       turtle.goTo(xpos,ypos) #paired
   =====
       turtle.pendown()
   =====
       for sides in range(4):    
   =====
       for sides in range(5):  #paired
   =====
           turtle.forward(width)     
   =====
           turtle.forward(100)  #paired
   =====      
           turtle.left(90) 
   =====      
           turtle.right(90) #paired