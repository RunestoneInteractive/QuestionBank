.. activecode:: 1306_cw1_f19_q1_unittest
    :author: Mohammad Rajiur Rahman
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0454545455
    :total_students_attempting: 22
    :num_students_correct: 11.0
    :mean_clicks_to_correct: 6.4545454545

    [20 pts] Write a Python program to request the user to type his/her first name and store it in a variable. 
    Then request the user to type his/her last name and store in a different variable. Then print a welcome 
    message (in a single line), which will look as follows for ``Jane Doe``
    
    Hi Jane Doe, you are in my first program!
    
    ~~~~
    # Write your program here
    
    
    
    =====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testMany(self):
            edText = self.getEditorText()
            outText = self.getOutput()
            outText = " ".join(outText.split())
            self.assertIn("print(", edText, "Testing for print functions")
            self.assertIn("Hi Jane Doe, you are in my first program!", outText, "Testing printout")
            self.assertIn("Jane", outText, "Testing printing first name")
            self.assertIn("Doe", outText, "Testing printing last name")
    
    myTests().main()