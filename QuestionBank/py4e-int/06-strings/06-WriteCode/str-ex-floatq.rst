.. activecode::  str-ex-floatq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :nocodelens:

    string = "X-DSPAM-Confidence: 0.8475"


    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(num,0.8475)

    myTests().main()