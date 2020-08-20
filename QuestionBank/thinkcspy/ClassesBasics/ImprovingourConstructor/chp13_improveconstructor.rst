.. codelens:: chp13_improveconstructor
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: ImprovingourConstructor
    :topics: ClassesBasics/ImprovingourConstructor
    :from_source: T

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self, initX, initY):
            """ Create a new point at the given coordinates. """
            self.x = initX
            self.y = initY

    p = Point(7, 6)