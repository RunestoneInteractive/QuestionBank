.. activecode:: LHSChapterSixteenQuestionOne
    :author: Wesley Thang
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Add a method ``reflect_x`` to ``Point`` which returns a new ``Point``, one which is the
    reflection of the point about the x-axis.  For example,
    ``Point(3, 5).reflect_x()`` is (3, -5)
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

            p1 = Point(3, 5).reflect_x()
            self.assertEqual(3, p1.getX(), "Checking point's x value")
            self.assertEqual(-5, p1.getY(), "Checking point's y value")

            p1 = Point(-3, 67).reflect_x()
            self.assertEqual(-3, p1.getX(), "Checking point's x value")
            self.assertEqual(-67, p1.getY(), "Checking point's y value")

    myTests().main()