.. activecode:: lhs_1_4
    :author: LHS CS Team
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.7130434783
    :total_students_attempting: 115
    :num_students_correct: 104.0
    :mean_clicks_to_correct: 1.5961538462

    Write code to assign the variable ``yb`` to have the same value that variable ``cw`` has. Do not change the first line of code (``cw = "Hello"``). Also, do not "hard code" the result by setting ``yb = "Hello"``. Instead, write code that would work no matter what the current value of ``cw`` is.
    ~~~~
    cw = "Hello"
    yb = 0
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(cw, yb, "Testing that yb has the same value as cw")
           self.assertEqual(cw, "Hello", "Testing that cw's value is 'Hello'.")           
    
    myTests().main()