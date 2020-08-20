.. activecode:: assess_question1_1_2_cofi_lad_2
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
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Write code to print out the phrase "Wile E. Coyote".
    ~~~~
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertIn("Wile E. Coyote", self.getOutput(), "Your output should contain a phrase Wile E. Coyote")
    
    myTests().main()