.. activecode:: exp1_q3_write
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.7746478873
   :total_students_attempting: 71
   :num_students_correct: 68.0
   :mean_clicks_to_correct: 1.3382352941

   Finish the function diffMaxMin to return the difference between the largest and smallest value in the passed list of numbers (nums). For example, diffMaxMin([1,2,3]) should return 2 since the difference between 3 and 1 is 2. 
   
   ~~~~
   def diffMaxMin(nums):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(diffMaxMin([1, 2, 3]), 2, 'diffMaxMin([1, 2, 3])')
           self.assertEqual(diffMaxMin([10, 20, 30]), 20, 'diffMaxMin([10, 20, 30])')
           self.assertEqual(diffMaxMin([1, 10]), 9, 'diffMaxMin([1 , 10])')
           self.assertEqual(diffMaxMin([10, 1]), 9, 'diffMaxMin([-10 , 1])')
           self.assertEqual(diffMaxMin([4, 1, 10]), 9, 'diffMaxMin([4, 1 , 10])')
           self.assertEqual(diffMaxMin([4, -10, 1]), 14, 'diffMaxMin([4, -10 , 1])')
            
           
   
   myTests().main()