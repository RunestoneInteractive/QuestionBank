.. activecode:: str-count-fixq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-count
    :topics: 06-strings/06-count
    :from_source: T
    :nocodelens:

    def count(text, aChar):
    lettercount = 0
        for c in text:
            if c != aChar:
                lettercount = lettercount + 3
    return lettercount

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(count('banana','a'),3,"Tested 'a' in 'banana'")
            self.assertEqual(count('pineapple','a'),1,"Tested 'a' in 'pineapple'")
            self.assertEqual(count('pepperoni pizza','p'),4,"Tested 'p' in 'pepperoni pizza'")
            self.assertEqual(count('racecar','r'),2,"Tested 'r' in 'racecar'")

    myTests().main()