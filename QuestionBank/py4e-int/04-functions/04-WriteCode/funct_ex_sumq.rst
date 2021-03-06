.. activecode:: funct_ex_sumq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Write a fruitful function ``sumTo(n)`` that returns the sum of all integer numbers up to and
    including `n`. So ``sumTo(10)`` would be ``1+2+3...+10`` which would return the value 55.
    Use the equation  (n * (n + 1)) / 2.
    ~~~~
    def sumTo(n):
        # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertAlmostEqual(sumTo(15),120.0,0,"Tested sumTo on input 15")
            self.assertAlmostEqual(sumTo(0),0.0,0,"Tested sumTo on input 0")
            self.assertAlmostEqual(sumTo(25),325.0,0,"Tested sumTo on input 25")
            self.assertAlmostEqual(sumTo(7),28.0,0,"Tested sumTo on input 7")

    myTests().main()