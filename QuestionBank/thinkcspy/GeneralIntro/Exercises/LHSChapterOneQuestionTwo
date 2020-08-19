.. activecode:: LHSChapterOneQuestionTwo
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4444444444
    :total_students_attempting: 18
    :num_students_correct: 14.0
    :mean_clicks_to_correct: 1.5714285714

    Fix the following code so that it displays ``My second program adds two numbers, 7 and 6:`` and the prints the correct value.
    ~~~~
    print("My first program adds two numbers, 2 and 3:")
    print(2 + 3)
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertIn('second', self.getOutput(), 'Testing output. (Looking for "second")')
            self.assertIn('7 and 6', self.getOutput(), 'Testing output. (Looking for "7 and 6")')
        def testTwo(self):
            self.assertIn('13', self.getOutput(), 'Testing output. (Looking for "13")')
    
    myTests().main()