.. activecode:: KDL_ch6_3
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.2142857143
   :total_students_attempting: 14
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 14.9285714286

   
   
   Use a for loop to roll a 10 sided dice three times. 
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('for', self.getEditorText(), 'contains for loop')
           self.assertIn('random.randrange(1,11)', self.getEditorText(), 'gets random')
           self.assertIn('range(3)', self.getEditorText(), 'loops 3 times')
   myTests().main()