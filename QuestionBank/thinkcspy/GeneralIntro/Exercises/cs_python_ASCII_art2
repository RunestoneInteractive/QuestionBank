.. activecode:: cs_python_ASCII_art2
    :author: Norm Prokup
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1764705882
    :total_students_attempting: 17
    :num_students_correct: 13.0
    :mean_clicks_to_correct: 3.3846153846

    Write code to display a face drawn with characters. (Use the print command!):
    
    The output you get should be:
    
    :: 
    
       (\___/)
       (=o.o=)
        ) ^ ( 
       /|| //\
      (")|/("))__//
    
    HINT: The backslash character \\ is special. To print a single backslash \\, you must enter two consecutive backslashes \\ \\ in your print statement. We'll discuss why later. 
    ~~~~
    # write your code below
    
    
    
    
    
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn( '(=o.o=)', self.getOutput(), "Testing output. (Checking for eyes.)") 
    
        def testTwo(self):
            self.assertIn( ') ^ (', self.getOutput(), "Testing output. (Checking for mouth.)") 
    
        def testThree(self):
            self.assertIn( '/|| //\\', self.getOutput(), "Testing output. (Checking for legs.)")           
    
        def testFour(self):
            self.assertIn( '(")|/("))', self.getOutput(), "Testing output. (Checking for feet.)")           
    
    myTests().main()