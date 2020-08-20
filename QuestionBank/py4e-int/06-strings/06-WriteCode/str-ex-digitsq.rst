.. activecode:: str-ex-digitsq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    def numDigits(n):
        # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(numDigits(2),1,"Tested numDigits on input of 2")
            self.assertEqual(numDigits(55),2,"Tested numDigits on input of 55")
            self.assertEqual(numDigits(1352),4,"Tested numDigits on input of 1352")
            self.assertEqual(numDigits(444),3,"Tested numDigits on input of 444")



    myTests().main()