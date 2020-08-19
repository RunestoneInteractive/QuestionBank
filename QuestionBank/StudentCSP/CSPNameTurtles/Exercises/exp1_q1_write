.. activecode:: exp1_q1_write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.4050632911
   :total_students_attempting: 79
   :num_students_correct: 61.0
   :mean_clicks_to_correct: 5.7540983607

   Finish the function below to return True if there are at least two items in the list nums that are adjacent and both equal to 2, otherwise return False.  For example, return True for [1, 2, 2] since there are two adjacent items equal to 2 (at index 1 and 2) and False for [2, 1, 2] since the 2's are not adjacent.
   
   ~~~~
   def has22(nums):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(has22([1, 2, 2]), True, 'has22([1, 2, 2])')
           self.assertEqual(has22([1, 2, 1, 2]), False, 'has22([1, 2, 1, 2])')
           self.assertEqual(has22([2, 1, 2]), False, 'has22([2, 1, 2])')
           self.assertEqual(has22([2, 2, 1]), True, 'has22([2, 2, 1])')
           self.assertEqual(has22([3, 4, 2]), False, 'has22([3, 4, 2])')
           self.assertEqual(has22([2]), False, 'has22([2])')
           self.assertEqual(has22([]), False, 'has22([])')
   
   myTests().main()