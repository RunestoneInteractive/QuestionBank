.. activecode:: funct_ex_triangleq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Change the code so the function takes parameters for the base and height of the triangle.
    Then, write code to call the function and print the result.
    ~~~~
    def areaTriangle():
        base = 5
        height = 4
        return (5 * 4) / 2

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(areaTriangle(12,45),270,"Tested areaTriangle on inputs 12 and 45")
            self.assertEqual(areaTriangle(5,4),10,"Tested areaTriangle on inputs 5 and 4")

    myTests().main()