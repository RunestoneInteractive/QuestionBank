.. activecode:: loop-sum-odd-write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: Exercises
   :topics: CSPRepeatNumbers/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.4012738854
   :total_students_attempting: 157
   :num_students_correct: 153.0
   :mean_clicks_to_correct: 4.2222222222

    Finish the function to return the sum of the odd numbers in the passed list.  For example, sum_odd([1,1,1]) returns 3 
    and sum_odd([2,4]) returns 0.  
   ~~~~
   def sum_odd(num_list):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(sum_odd([1,1,1]), 3,"sum_odd([1,1,1]")
           self.assertEqual(sum_odd([2,4]), 0,"sum_odd([2,4]")
           self.assertEqual(sum_odd([2,4,1]), 1,"sum_odd([2,4,1]")
           self.assertEqual(sum_odd([3]), 3,"sum_odd([3]")
           self.assertEqual(sum_odd([3, 5, 4]), 8,"sum_odd([3,5,4]")
              
   myTests().main()