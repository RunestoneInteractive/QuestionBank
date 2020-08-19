.. activecode:: itr-ex-countq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-WriteCode
    :topics: 05-iterations/05-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    output = ""
    x = -10
    while x < 0
        x = x - 1
    output = output + str(x) + " "
    print(output)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(output,"-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 ")

    myTests().main()