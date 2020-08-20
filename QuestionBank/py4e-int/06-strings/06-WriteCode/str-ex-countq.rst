.. activecode::  str-ex-countq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :nocodelens:

    Create a function named ``count`` that accepts a string and a letter
    as arguments, then returns the count of that letter in the string.
    For example, if the function call was count("banana", "a") it would
    return 3.
    ~~~~

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(count('banana','a'),3,"Tested 'a' in 'banana'")
            self.assertEqual(count('pineapple','s'),0,"Tested 's' in 'pineapple'")
            self.assertEqual(count('pepperoni pizza','p'),4,"Tested 'p' in 'pepperoni pizza'")
            self.assertEqual(count('racecar','r'),2,"Tested 'r' in 'racecar'")

    myTests().main()