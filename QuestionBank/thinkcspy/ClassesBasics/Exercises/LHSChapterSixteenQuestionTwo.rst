.. activecode:: LHSChapterSixteenQuestionTwo
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    The equation of a straight line is  "y = ax + b", (or perhaps "y = mx + b").
    The coefficients ``a`` and ``b`` completely describe the line.  Write a method in the
    ``Point`` class so that if a point instance is given another point, it will compute the equation
    of the straight line joining the two points.  It must return the two coefficients as a tuple
    of two values.  For example,   ::

       >>> print(Point(4, 11).get_line_to(Point(6, 15)))
       >>> (2, 3)

    This tells us that the equation of the line joining the two points is "y = 2x + 3".
    When will your method fail?
    ~~~~
    class Point:

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

    def main():
        #Your test code here
        
    if __name__ == "__main__":
        main()
    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return

            print('Auto-testing...')

            p1 = Point(4, 11)
            p2 = Point(6, 15)
            self.assertEqual(p1.get_line_to(p2), (2, 3), "Checking get_line_to")

            p1 = Point(2, 1)
            p2 = Point(6, 5)
            self.assertEqual(p1.get_line_to(p2), (1, -1), "Checking get_line_to")

    myTests().main()