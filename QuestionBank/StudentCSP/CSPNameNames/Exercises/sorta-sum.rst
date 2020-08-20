.. activecode:: sorta-sum
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.4468085106
       :total_students_attempting: 47
       :num_students_correct: 44.0
       :mean_clicks_to_correct: 2.6136363636

       
       Given 2 ints, a and b, return their sum. However, sums in the range 10..19
       inclusive, are forbidden, so in that case just return 20.  For example, 
       sorta_sum(3,4) returns 7 and sorta_sum(9, 4) returns 20.  
       ~~~~
       def sorta_sum(a,b):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(sorta_sum(3,4), 7, 'sorta_sum(3,4)')
               self.assertEqual(sorta_sum(9,4), 20, 'sorta_sum(9,4)')
               self.assertEqual(sorta_sum(10,11), 21, 'sorta_sum(10,11)')
               self.assertEqual(sorta_sum(12,-3), 9, 'sorta_sum(12,-3)')
               self.assertEqual(sorta_sum(-3, 12), 9, 'sorta_sum(-3, 12)')
               self.assertEqual(sorta_sum(4,5), 9, 'sorta_sum(4,5)')
               self.assertEqual(sorta_sum(4,6),20, 'sorta_sum(4,6)')
               self.assertEqual(sorta_sum(14,7),21, 'sorta_sum(14,7)')
               self.assertEqual(sorta_sum(14,6), 20, 'sorta_sum(14,6)')
               self.assertEqual(sorta_sum(10,9),20, 'sorta_sum(10,9)')
               self.assertEqual(sorta_sum(10,10), 20, 'sorta_sum(10,10)')
       
       myTests().main()