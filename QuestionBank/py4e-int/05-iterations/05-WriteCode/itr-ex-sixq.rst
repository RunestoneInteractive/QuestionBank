.. activecode:: itr-ex-sixq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-WriteCode
    :topics: 05-iterations/05-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    x = 3
    i = 0
    while i < 3:
        x =
        i = i + 1
    print()

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(x,6)

    myTests().main()