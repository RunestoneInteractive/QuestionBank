.. activecode:: funct_ex_squareq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Fix the 5 errors so the following code runs and returns the area of a square.
    ~~~~
    Def squareArea(sideLength)
        area = length * length
        return squareArea


    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(squareArea(10),100,"Tested squareArea on input 10")
            self.assertEqual(squareArea(23),529,"Tested squareArea on input 23")

    myTests().main()