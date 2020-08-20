.. activecode:: ch_c2_4
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: ClassesDiggingDeeper
   :subchapter: Exercises
   :topics: ClassesDiggingDeeper/Exercises
   :from_source: None

   class Point:
       def __init__(self, initX, initY):
           self.__x = initX
           self.__y = initY

       @property
       def x(self):
           return self.__x

       @property
       def y(self):
           return self.__y

       def scale(self, val):
           """ Return a new point that is self multiplied by val """
           return Point(self.__x * val, self.__y * val)

   if __name__ == "__main__":
       import test
       a = Point(7, -3)
       b = a.scale(2)
       test.testEqual(b.x,14)
       test.testEqual(b.y,-6)