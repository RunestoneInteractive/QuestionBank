.. activecode:: LHSChapterOneQuestionOne
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.9444444444
    :total_students_attempting: 18
    :num_students_correct: 17.0
    :mean_clicks_to_correct: 1.0

    The variable ``tpa`` currently has the value ``0``. Assign the variable ``tpa`` the value ``6`` .
    ~~~~
    tpa = 0
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(tpa, 6, "Testing that tpa's value is 6.")
    
    myTests().main()