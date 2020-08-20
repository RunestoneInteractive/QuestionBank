.. activecode::  cndtnl-wc-payq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-WriteCode
    :topics: 03-conditional/03-WriteCode
    :from_source: T
    :nocodelens:

    hours = 45
    rate = 10
    overtimeRate =  #your code here
    grossPay = 0
    if hours  #your code here
        grossPay = hours * rate
    else:
        overTime =  #your code here
        grossPay =  #your code here
    print(grossPay)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(grossPay, 475.0)

    myTests().main()