.. actex:: CS152_isValid_YNM_1
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens:

    Write a function called ``is_validYNM(aString)`` that takes a string as an argument
    and returns ``True`` if the argument is one of **"yes"**, **"no"** or **"maybe"** and ``False`` if
    it is anything else.
    ~~~~

    def is_validYNM(aString):
        # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
         def testOne(self):
             self.assertEqual(is_validYNM("yes"),True,"yes")
             self.assertEqual(is_validYNM("no"),True,"no")
             self.assertEqual(is_validYNM("maybe"),True,"maybe")
             self.assertEqual(is_validYNM("say what?"),False,"say what?")
             self.assertEqual(is_validYNM(""),False,"''")
             self.assertEqual(is_validYNM("ye"),False,"ye")
             self.assertEqual(is_validYNM("may"),False,"may")

    myTests().main()