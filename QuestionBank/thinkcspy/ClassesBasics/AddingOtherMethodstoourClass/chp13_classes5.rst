.. activecode:: chp13_classes5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: AddingOtherMethodstoourClass
    :topics: ClassesBasics/AddingOtherMethodstoourClass
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


    p = Point(7, 6)
    print(p.distanceFromOrigin())