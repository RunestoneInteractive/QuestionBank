.. parsonsprob:: mt1-rect-turtle-class
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: Exercises
   :topics: CSPIntroData/Exercises
   :from_source: F
   :numbered: left

   Solve my really cool parsons problem...if you can.
   -----
   from turtle import *
   =====
   class RectTurtle(Turtle):
   =====
   class RectTurtle(): #paired
   =====
       def draw_rectangle(self, xpos, ypos, width, height):
   =====
       def draw_rectangle(turtle, xpos, ypos, width, height): #paired
   =====
           self.setheading(0)
           self.penup()
           self.goto(xpos,ypos)
           self.pendown()
   =====
           for i in range(2):
   =====
               self.forward(width)
               self.right(90)
   =====
               self.forward(height)
               self.right(90)
   =====  
   def main():
   =====
      space = Screen()
   =====
      t = RectTurtle()
   =====
      t = Turtle() #paired
   =====
      t.draw_rectangle(0,0,100,50)
   =====
      draw_rectangle(t,0,0,100,50) #paired