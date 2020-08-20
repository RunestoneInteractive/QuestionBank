.. activecode:: asu_cs_func_q1
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.7857142857
    :total_students_attempting: 14
    :num_students_correct: 13.0
    :mean_clicks_to_correct: 2.8461538462

    Write a function that given a distance in miles, converts the distance to kilometers and returns. Assume that:
    
    ``miles = kilometers x 0.6``
    
    ~~~~
    def kilometers(mi):
        # Put your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):    
                
        def testOne(self):
            self.assertEqual(int(kilometers(60.0)), 60/0.6, "Testing 60mi")
            self.assertEqual(int(kilometers(600.0)), 600/0.6, "Testing 600mi")
        
    myTests().main()