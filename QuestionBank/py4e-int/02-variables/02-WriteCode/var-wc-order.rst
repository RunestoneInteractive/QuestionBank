.. activecode:: var-wc-order
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: 02-WriteCode
    :topics: 02-variables/02-WriteCode
    :from_source: T

    Add parentheses to the following code so that the total equals 40.

    ~~~~

    total = 7 + 3 * 6 - 2
    print(total)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(total,40)

    myTests().main()