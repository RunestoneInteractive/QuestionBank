.. activecode:: ch_cl_ex_3_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
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

        def slope_from_origin(self):
            if self.x == 0:
               return None
            else:
               return self.y / self.x


    p = Point(4, 10)
    print(p.slope_from_origin())