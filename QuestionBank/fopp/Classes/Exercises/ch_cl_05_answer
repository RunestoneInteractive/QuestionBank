.. activecode:: ch_cl_05_answer
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F

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

        def move(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy

        def __str__(self):
            return str(self.x)+","+str(self.y)


    p = Point(7,6)
    print(p)
    p.move(5,10)
    print(p)