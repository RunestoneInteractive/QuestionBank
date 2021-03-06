.. activecode:: LHSChapterSixteenQuestionEight
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Create a class called ``Animal`` that has two instance variables: ``arms`` and ``legs``.
    Create a class method called ``limbs`` that, when called, returns the total number of
    limbs the animal has. To the variable name ``spider``, assign an instance of ``Animal``
    that has 4 arms and 4 legs. Call the ``limbs`` method on ``spider`` and save the
    result to the variable name ``spidlimbs``. 

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
            self.assertEqual(spider.arms, 4, "Testing that spider was assigned the correct number of arms.")
            self.assertEqual(spider.legs, 4, "Testing that spider was assigned the correct number of legs.")
            self.assertEqual(spidlimbs, 8, "Testing that spidlimbs was assigned correctly.")
         
    myTests().main()