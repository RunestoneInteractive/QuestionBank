.. activecode:: LHSChapterOneQuestionTwoA
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.625
    :total_students_attempting: 16
    :num_students_correct: 11.0
    :mean_clicks_to_correct: 1.0909090909

    Write code to display a face drawn with characters. (Use the print command!):
    
    The output you get should be:
    
    :: 
    
         xxxxx
        x     x
       (  o o  )
        |  V  |
        | === |
         ----- 
    
    ~~~~
    # write your code below
    
    
    
    
    
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn( 'o o', self.getOutput(), "Testing output. (Checking for eyes.)") 
    
        def testTwo(self):
            self.assertIn( 'V', self.getOutput(), "Testing output. (Checking for nose.)") 
    
        def testThree(self):
            self.assertIn( '===', self.getOutput(), "Testing output. (Checking for mouth.)")           
    
    myTests().main()