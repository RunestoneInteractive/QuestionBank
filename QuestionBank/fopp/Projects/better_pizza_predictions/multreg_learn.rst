.. activecode:: multreg_learn
    :author: bmiller
    :difficulty: 2.0602409639
    :basecourse: fopp
    :chapter: Projects
    :subchapter: better_pizza_predictions
    :topics: Projects/better_pizza_predictions
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 32
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 19.0

    import sys
    # Give this program more time to run
    sys.setExecutionLimit(60000)
    
    def fit():
        # your code here
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
       # [1.18750070681955, 1.010416621897852, 0.39583316275729197]
       def testOne(self):
           res = fit()
           self.assertAlmostEqual(res[0], 1.1875, 2)
           self.assertAlmostEqual(res[1], 1.0104, 2)
           self.assertAlmostEqual(res[2], 0.3958, 2)
    
    myTests().main()