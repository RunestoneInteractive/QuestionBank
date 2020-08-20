.. activecode:: c1n
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: PointClass
    :topics: ClassesBasics/PointClass
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


    p = Point(3, 4)
    q = Point(5, 12)
    print(p)
    print(q)

    mid = p.halfway(q)

    print(mid)
    print(mid.getX())
    print(mid.getY())