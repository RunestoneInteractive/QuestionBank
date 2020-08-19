.. activecode:: int-ex-inclusiveq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-WriteCode
    :topics: 05-iterations/05-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    def sumFunc(start, stop):
        sum = 0
        for num in range(start, stop + 1):
            sum = sum + num
        return sum

    print(sumFunc(1,10))

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(sumFunc(1, 10),55,"Tested sumFunc on inputs 1 and 10")
            self.assertEqual(sumFunc(10, 3),0,"Tested sumFunc on inputs 10 and 3")
            self.assertEqual(sumFunc(-5, 0),-15,"Tested sumFunc on inputs 20 and 50")
            self.assertEqual(sumFunc(-3, 12),72,"Tested sumFunc on inputs -3 and 12")

    myTests().main()