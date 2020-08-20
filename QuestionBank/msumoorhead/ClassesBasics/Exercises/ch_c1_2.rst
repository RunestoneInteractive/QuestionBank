.. activecode:: ch_c1_2
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: ClassesBasics
   :subchapter: Exercises
   :topics: ClassesBasics/Exercises
   :from_source: None

   class Point:

       def __init__(self, initX, initY):
           """ Create a new point at the given coordinates """
           self.__x = initX
           self.__y = initY

       def getX(self):
           """ Get its x coordinate """
           return self.__x

       def getY(self):
           """ Get its y coordinate """
           return self.__y

       def __str__(self):
           """ Return a string representation of the point """
           return "({}, {})".format(self.__x, self.__y)

       def halfway(self, other):
           """ Create a point halfway between self and other """
           mx = (self.__x + other.__x) / 2
           my = (self.__y + other.__y) / 2
           return Point(mx, my)

       def distFromOrigin(self):
           """ Return the distance from self to (0,0) """
           return (self.__x**2 + self.__y**2)**0.5

       def distFrom(self, other):
           """ Return the distance from self to other """


   if __name__ == "__main__":
       import test