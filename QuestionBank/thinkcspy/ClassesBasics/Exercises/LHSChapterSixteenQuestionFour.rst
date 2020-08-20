.. activecode:: LHSChapterSixteenQuestionFour
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Create a class called ``inst_var`` that defines two instance variables: ``num1`` and ``num2``.
    Then, create an instance where ``num1`` is 6 and ``num2`` is 10 and save this instance to the
    variable ``t``. 
    ~~~~
    #Define the class here

    
    #Your test code here
    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return

        def testOneA(self):
            self.assertEqual(t.num1, 6, "Testing that t.num1 has correct number assigned.")
        def testOneB(self):
            self.assertEqual(t.num2, 10, "Testing that t.num2 has correct number assigned.")

    myTests().main()