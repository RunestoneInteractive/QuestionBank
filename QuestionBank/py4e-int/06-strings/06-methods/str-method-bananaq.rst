.. activecode::  str-method-bananaq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-methods
    :topics: 06-strings/06-methods
    :from_source: T
    :nocodelens:

    def countSS(word):
        sCounter is word.count('s')
        return Counter

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(countSS('banana'),0,"Tested countSS on input 'banana'")
            self.assertEqual(countSS('Mississippi'),2,"Tested countSS on input 'Mississippi'")
            self.assertEqual(countSS('scissors'),1,"Tested countSS on input 'scissors'")
            self.assertEqual(countSS('methods'),0,"Tested countSS on input 'methods'")

    myTests().main()