.. activecode:: chp13_classes2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: UserDefinedClasses
    :topics: ClassesBasics/UserDefinedClasses
    :from_source: T

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self):
            """ Create a new point at the origin """
            self.x = 0
            self.y = 0

    p = Point()         # Instantiate an object of type Point
    q = Point()         # and make a second point

    print(p)
    print(q)

    print(p is q)