.. activecode:: assess_question1_1_2
    :author: bmiller
    :difficulty: 1.027395368
    :basecourse: fopp
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: T
    :language: python
    :autograde: unittest
    :pct_on_first: 0.7090715804
    :total_students_attempting: 2822
    :num_students_correct: 2636.0
    :mean_clicks_to_correct: 1.4650986343

    Write code to print out the phrase "Hello World".
    ~~~~
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertIn("Hello World", self.getOutput(), "Your output should contain a phrase Hello World")
    
    myTests().main()