.. activecode:: assess_question1_1_2_cofi_lad
    :author: Lynda Danielson
    :difficulty: 1.0
    :basecourse: fopp
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 3
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 1.0

    Write code to print out the phrase "Go Yotes!".
    ~~~~
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertIn("Go Yotes!", self.getOutput(), "Your output should contain a phrase Go Yotes!")
    
    myTests().main()