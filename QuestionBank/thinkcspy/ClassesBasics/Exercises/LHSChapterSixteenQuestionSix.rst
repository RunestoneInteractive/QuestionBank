.. activecode:: LHSChapterSixteenQuestionSix
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Create a class called ``math_op`` with one instance variable and a method. The
    instance variable should be ``numb``. The method should be called ``squared`` and
    return the instance variable squared. Create an instance of this class with an
    initial number of 8. Assign to the variable ``output`` the value of the square of the ``numb`` without
    hardcoding. Call the method so that the value which is returned is 64.
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

        def testOne(self):
            self.assertEqual(output, 64, "Testing that output has correct value assigned.")
         
    myTests().main()