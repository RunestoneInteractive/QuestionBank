.. activecode:: lhs_3_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Debugging
    :subchapter: Exercises
    :topics: Debugging/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.1135531136
    :total_students_attempting: 546
    :num_students_correct: 506.0
    :mean_clicks_to_correct: 4.8280632411

    This program calculates how far an object will fall (in feet) in a given number of seconds. However, it does not produce the correct answer. Find and fix the error:
    
    ~~~~
    g = 32.174;
    
    t = input( "Enter the number of seconds: " )
    d = 1 // 2 * g * t**2
    print( "The brick fell ", d, " feet in ", t, " seconds." )
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            dist = 1 / 2 * g * t**2
            self.assertIn('The brick fell  ' + str(dist) + '  feet in  ' + str(t) + '  seconds.', self.getOutput(), "Actual is the correct answer. Expected is your program output")
    
    myTests().main()