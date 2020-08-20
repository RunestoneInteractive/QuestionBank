.. activecode:: KDL_ch6_6
   :author: Kaelyn Leake
   :difficulty: 1.0636415393
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.3043478261
   :total_students_attempting: 138
   :num_students_correct: 87.0
   :mean_clicks_to_correct: 2.0804597701

   Use indexing to determine the first location of 5 in the list and save this as ``i``. Determine the number of times 5` is present and save this as ``c``. No for loop is needed. Don't hardcode the answers I'm going to run it for a different L.
   ~~~~
   L=[6,3,6,8,3,5,6,3,5,7,3,5,6]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertNotIn('i=5', self.getEditorText(), 'Not hardcoded')
           self.assertNotIn('c=3', self.getEditorText(), 'Not hardcoded')
           self.assertEqual(i, L.index(5), "Testing for correct i value")
           self.assertEqual(c, L.count(5), "Testing for correct c value")
           
   myTests().main()