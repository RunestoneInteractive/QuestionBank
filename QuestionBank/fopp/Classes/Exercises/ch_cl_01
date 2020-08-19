.. actex:: ch_cl_01
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Classes
   :subchapter: Exercises
   :topics: Classes/Exercises
   :from_source: T

   Add a method ``reflect_x`` to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, ``Point(3, 5).reflect_x()`` is (3, -5)

   ~~~~

   class Point:
       """ Point class for representing and manipulating x,y coordinates. """

       def __init__(self, initX, initY):

           self.x = initX
           self.y = initY

       def getX(self):
           return self.x

       def getY(self):
           return self.y

       def distanceFromOrigin(self):
           return ((self.x ** 2) + (self.y ** 2)) ** 0.5

       def move(self, dx, dy):
           self.x = self.x + dx
           self.y = self.y + dy

       def __str__(self):
           return str(self.x)+","+str(self.y)