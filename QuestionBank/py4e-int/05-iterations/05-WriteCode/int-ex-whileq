.. activecode:: int-ex-whileq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-WriteCode
    :topics: 05-iterations/05-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Rewrite the following code to use a while loop instead of a for loop.
    ~~~~
    product = 1  # Start out with nothing
    numbers = range(1,11)
    for number in numbers:
        product = product * number
    print(product)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(product, 3628800)

    myTests().main()