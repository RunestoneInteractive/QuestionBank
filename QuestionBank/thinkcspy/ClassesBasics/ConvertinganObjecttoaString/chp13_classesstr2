.. activecode:: chp13_classesstr2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: ConvertinganObjecttoaString
    :topics: ClassesBasics/ConvertinganObjecttoaString
    :from_source: T

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self, initX, initY):
            """ Create a new point at the given coordinates. """
            self.x = initX
            self.y = initY

        def getX(self):
            return self.x

        def getY(self):
            return self.y

        def distanceFromOrigin(self):
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5

        def __str__(self):
            return "x=" + str(self.x) + ", y=" + str(self.y)

    p = Point(7, 6)
    print(p)