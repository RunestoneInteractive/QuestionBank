.. activecode:: ch_c2_1
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: ClassesDiggingDeeper
   :subchapter: Exercises
   :topics: ClassesDiggingDeeper/Exercises
   :from_source: None

   class Rectangle:
       def __init__(self,start,width,height):
           self.__start = start
           self.__width = width
           self.__height = height

       def getWidth(self):
           return self.__width

       def getHeight(self):
           return self.__height

       def getStartPoint(self):
           return self.__start

       def __str__(self):
           return 'start={} w={} h={}'.format(str(self.__start),self.__width,self.__height)

       def area(self):
           return self.__width * self.__height

       def perimeter(self):
           return (self.__width + self.__height) * 2