.. activecode:: funct-ex-perimeterq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Fix the 4 errors so the following code runs and returns the perimeter of a rectangle.
    ~~~~
    def recPerimeter(length, width)
    perimeter = 2 * (length + width)
        Return recPerimeter

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(recPerimeter(10, 20),60,"Tested recPerimeter on inputs 10 and 20")
            self.assertEqual(recPerimeter(1, 2),6,"Tested recPerimeter on inputs 1 and 2")
            self.assertEqual(recPerimeter(23.2, 12.3),71,"Tested recPerimeter on inputs 23.2 and 12.3")
            self.assertEqual(recPerimeter(3.0, 2),10.0,"Tested recPerimeter on inputs 3.0 and 2")

    myTests().main()