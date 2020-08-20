.. activecode:: ch_c1_6
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

       def __str__(self):
           """ Return a string representation of the point """
           return "({}, {})".format(self.__x, self.__y)

   # your code goes here