.. activecode:: chp13_classesmid1
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: InstancesasReturnValues
    :topics: ClassesBasics/InstancesasReturnValues
    :from_source: None

    class Point:

        def __init__(self, initX, initY):
            """ Create a new point at the given coordinates. """
            self.__x = initX
            self.__y = initY

        def getX(self):
            return self.__x

        def getY(self):
            return self.__y

        def distanceFromOrigin(self):
            return ((self.__x ** 2) + (self.__y ** 2)) ** 0.5

        def __str__(self):
            return "x=" + str(self.__x) + ", y=" + str(self.__y)

        def halfway(self, target):
             mx = (self.__x + target.__x) / 2
             my = (self.__y + target.__y) / 2
             return Point(mx, my)

    p = Point(3, 4)
    q = Point(5, 12)
    mid = p.halfway(q)

    print(mid)
    print(mid.getX())
    print(mid.getY())