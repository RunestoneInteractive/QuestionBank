.. activecode:: MSIT-2-12F
    :author: Kevin Austin
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5
    :total_students_attempting: 4
    :num_students_correct: 4.0
    :mean_clicks_to_correct: 3.0

    The goal of this exercise is to exchange the values stored in two variables.  
    The code given below assigns the number 27 to var1 and the string "yes" to var2.  
    Add statements to the program so in the end, var1 contains "yes" and var2 contains 27.  
    Do NOT hard code your solution.  (HINT: you will need to create a new variable to hold one of the values temporarily)
    ~~~~
    # do not hard code the solution
    var1 = 27
    var2 = "yes"
    # add your code after this line (requires no less than three statements)
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(var1, "yes", "Testing that var1 has the original value held by var2")
           self.assertEqual(var2, 27, "Testing that var2 has the original value held by var1")           
    
    myTests().main()