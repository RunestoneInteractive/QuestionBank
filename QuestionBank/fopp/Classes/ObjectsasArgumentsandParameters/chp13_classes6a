.. activecode:: chp13_classes6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: ObjectsasArgumentsandParameters
    :topics: Classes/ObjectsasArgumentsandParameters
    :from_source: T

    import math

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

        def distance(self, point2):
            xdiff = point2.getX()-self.getX()
            ydiff = point2.getY()-self.getY()

            dist = math.sqrt(xdiff**2 + ydiff**2)
            return dist

    p = Point(4,3)
    q = Point(0,0)
    print(p.distance(q))