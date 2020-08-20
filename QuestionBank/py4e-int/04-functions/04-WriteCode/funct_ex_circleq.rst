.. activecode:: funct_ex_circleq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Write a function ``areaOfCircle(r)``` which returns the area of a circle of radius `r`.
    Make sure you import the math module in your solution.
    ~~~~
    def areaOfCircle(r):
        # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertAlmostEqual(areaOfCircle(5.0),78.53981633974483,5,"Tested input: areaOfCircle(5.0)")
            self.assertEqual(areaOfCircle(5.0),78.53981633974483,"Tested input: areaOfCircle(5.0)")
            self.assertEqual(areaOfCircle(0),0.0,"Tested input: areaOfCircle(0)")
            self.assertAlmostEqual(areaOfCircle(31415.926535897932),3100627668.0299816,5,"Tested input: areaOfCircle(31415.926535897932)")


    myTests().main()