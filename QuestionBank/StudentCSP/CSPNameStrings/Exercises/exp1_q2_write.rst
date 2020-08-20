.. activecode:: exp1_q2_write
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameStrings
   :subchapter: Exercises
   :topics: CSPNameStrings/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.3863636364
   :total_students_attempting: 88
   :num_students_correct: 76.0
   :mean_clicks_to_correct: 3.3552631579

   Finish the function to define countInRange that returns a count of the number of times that a target value appears in a list between the start and end indices (inclusive). For example, countInRange(1,2,4,[1, 2, 1, 1, 1, 1]) should return 3 since there are three 1's between index 2 and 4 inclusive.
   
   
   ~~~~
   def countInRange(target, start, end, numList):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(countInRange(2, 0, 2, [1, 2, 2]), 2, 'countInRange(2, 0, 2, [1, 2, 2])')
           self.assertEqual(countInRange(1, 2, 4, [1, 2, 1, 1, 1, 1]), 3, 'countInRange(1, 2, 4, [1, 2, 1, 1, 1, 1])')
           self.assertEqual(countInRange(1, 0, 4, [1, 2, 1, 1, 1, 1]), 4, 'countInRange(1, 0, 4, [1, 2, 1, 1, 1, 1])')
           self.assertEqual(countInRange(2, 1, 2, [1, 2, 2]), 2, 'countInRange(2, 1, 2, [1, 2, 2])')
           self.assertEqual(countInRange(3, 1, 2, [1, 2, 2]), 0, 'countInRange(3, 1, 2, [1, 2, 2])')
           self.assertEqual(countInRange(3, 1, 2, [3, 3, 3, 3]), 2, 'countInRange(3, 1, 2, [3, 3, 3, 3])')
           
   
   myTests().main()