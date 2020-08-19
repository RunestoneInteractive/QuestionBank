.. activecode:: lhs_2_12a
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
    :pct_on_first: 0.5133819951
    :total_students_attempting: 411
    :num_students_correct: 395.0
    :mean_clicks_to_correct: 2.5848101266

    Modify the following program so that it will convert degrees fahrenheit to degrees celsius (change the ``deg_c`` assignment in ``f_to_c``).
    
    Only line 3 of the program needs to be changed.
    ~~~~
    def f_to_c (deg_f):
        # formula to convert F to C is: ((degrees Fahrenheit ) minus 32) times (5/9) 
        deg_c = 0 # ---Fix this---
        return deg_c
    
    deg_f = float(input("What is the temperature in Fahrenheit ? "))
    
    print(deg_f, " degrees Fahrenheit is ", f_to_c( deg_f ), " degrees Celsius .")
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertAlmostEqual (  f_to_c( 98.6 ), 37, 2,"Testing that f_to_c(98.6) = 37") 
    
    myTests().main()