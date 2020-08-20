.. activecode:: c1m
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
            """ Return a string representation of self """
            return "({}, {})".format(self.__x, self.__y)

        def distFromOrigin(self):
            """ Return the distance between self and (0,0) """
            return 0


    if __name__ == "__main__":
        import test
        a = Point(-4,3)
        test.testEqual(a.distFromOrigin(), 5)

        b = Point(1,1)
        test.testEqual(b.distFromOrigin(), 2**0.5)