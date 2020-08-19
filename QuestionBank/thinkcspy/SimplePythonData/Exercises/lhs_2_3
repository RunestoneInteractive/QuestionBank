.. activecode:: lhs_2_3
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.5339578454
    :total_students_attempting: 427
    :num_students_correct: 405.0
    :mean_clicks_to_correct: 2.4049382716

    Write code to print out the type of the variable ``apples_and_oranges``, the type of the variable ``abc``, and the type of the variable ``new_var``. (Use the print command!)
    ~~~~
    apples_and_oranges = """hello, everybody
                               how're you?"""
    
    abc = 6.75483
    
    new_var = 824
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn('print', self.getEditorText(), "Testing that 'print' is in the code. (Don't worry about Actual and Expected Values.)")
            self.assertIn('class', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           
            self.assertIn('str', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           
            self.assertIn('int', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           
            self.assertIn('float', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           
    
    myTests().main()