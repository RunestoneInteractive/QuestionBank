.. activecode:: chp13_classes1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: UserDefinedClasses
    :topics: Classes/UserDefinedClasses
    :from_source: T

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self):

            self.x = 0
            self.y = 0

    p = Point()         # Instantiate an object of type Point
    q = Point()         # and make a second point

    print("Nothing seems to have happened with the points")