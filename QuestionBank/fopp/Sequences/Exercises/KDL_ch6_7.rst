.. activecode:: KDL_ch6_7
   :author: Kaelyn Leake
   :difficulty: 1.1084143337
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1707317073
   :total_students_attempting: 123
   :num_students_correct: 69.0
   :mean_clicks_to_correct: 2.8405797101

   Use indexing to print the 6th through 9th values in the supplied list (there should be 4 total, traditional counting). Save the result to variable ``i``. Don't hardcode the result...I'm going to change L for my run!
   ~~~~
   L=[6,3,6,8,3,5,6,3,5,7,3,5,6]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           def pullout(l):
               return l[5:9]
           self.assertIn('print(', self.getEditorText(), 'Contains print')
           self.assertNotIn('[5,6,3,5]', self.getEditorText(), 'Not hardcoded')
           self.assertEqual(i, pullout(L), "Testing for correct i value")
   
           
   myTests().main()