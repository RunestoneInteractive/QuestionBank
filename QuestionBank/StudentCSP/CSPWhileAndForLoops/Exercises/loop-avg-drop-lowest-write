.. activecode:: loop-avg-drop-lowest-write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.102739726
   :total_students_attempting: 146
   :num_students_correct: 124.0
   :mean_clicks_to_correct: 9.4032258065

   Finish the function to return the average of a list of numbers, but drop the lowest value. However, 
   if the list only has one value then return that.  For example, get_avg_drop_lowest([90]) returns 90 and 
   get_avg_drop_lowest([90, 10]) also returns 90. 
   ~~~~
   def get_avg_drop_lowest(num_list):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(get_avg_drop_lowest([90]), 90, "get_avg_drop_lowest([90])")
           self.assertEqual(get_avg_drop_lowest([90, 10]), 90, "get_avg_drop_lowest([90, 10])")
           self.assertEqual(get_avg_drop_lowest([20, -20, 20]), 20, "get_avg_drop_lowest([20, -20, 20])")
           self.assertEqual(get_avg_drop_lowest([70, 80, 100]), 90, "get_avg_drop_lowest([70, 80, 100])")
           self.assertEqual(get_avg_drop_lowest([75, 83, 90]), 86.5, "get_avg_drop_lowest([75, 83, 90])")
              
   myTests().main()