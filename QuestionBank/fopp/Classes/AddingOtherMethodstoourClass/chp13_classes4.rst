.. activecode:: chp13_classes4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: AddingOtherMethodstoourClass
    :topics: Classes/AddingOtherMethodstoourClass
    :from_source: T

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self, initX, initY):

            self.x = initX
            self.y = initY

        def getX(self):
            return self.x

        def getY(self):
            return self.y


    p = Point(7,6)
    print(p.getX())
    print(p.getY())