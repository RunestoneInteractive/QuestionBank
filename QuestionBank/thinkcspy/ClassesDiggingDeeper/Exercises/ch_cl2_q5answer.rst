.. activecode:: ch_cl2_q5answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
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

        def __str__(self):
            return "x=" + str(self.x) + ", y=" + str(self.y)


    class Rectangle:
        """Rectangle class using Point, width and height"""

        def __init__(self, initP, initW, initH):

            self.location = initP
            self.width = initW
            self.height = initH

        def transpose(self):
            temp = self.width
            self.width = self.height
            self.height = temp