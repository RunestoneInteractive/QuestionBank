.. activecode:: var-wc-fruitq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: 02-WriteCode
    :topics: 02-variables/02-WriteCode
    :from_source: T

    Let's say that apples are $0.40 apiece, and pears are $0.65 apiece.
    Modify the program below to calculate the total cost of 4 apples and 3 pears

    ~~~~

    apples = 4
    pears = 3
    totalCost =
    print(totalCost)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(totalCost,3.55, "totalCost should equal 3.55")

    myTests().main()