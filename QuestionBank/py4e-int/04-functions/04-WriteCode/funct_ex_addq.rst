.. activecode:: funct_ex_addq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Rewrite the function ``sumTo(n)`` that returns the sum of all integer
    numbers up to and including `n`. This time use the accumulator pattern.
    ~~~~
    def sumTo(n):
        # your code here

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(sumTo(15),120,"Tested sumTo on input 15")
            self.assertEqual(sumTo(0),0,"Tested sumTo on input 0")
            self.assertEqual(sumTo(25),325,"Tested sumTo on input 25")
            self.assertEqual(sumTo(7),28,"Tested sumTo on input 7")

    myTests().main()