.. activecode:: multreg_dot
    :author: bmiller
    :difficulty: 1.4515841142
    :basecourse: fopp
    :chapter: Projects
    :subchapter: better_pizza_predictions
    :topics: Projects/better_pizza_predictions
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 31
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 8.6666666667

    def dot(a,b):
        # your code here
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
       def testOne(self):
           self.assertEqual(dot([1,2,3],[4,5,6]), 32, "testing [1,2,3] and [4,5,6]")
           self.assertEqual(dot([0,0,0],[4,5,6]), 0, "testing with one vector all 0's")
           self.assertEqual(dot([1,1,1],[1,1,1]), 3, "testing vectors of all 1's ")
           self.assertEqual(dot([1,1,1],[-1,-1,-1]), 0, "testing vectors of all 1's and -1's ")
    
    myTests().main()