.. activecode:: KDL_ch14_3
   :author: Kaelyn Leake
   :difficulty: 1.1963409192
   :basecourse: fopp
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1
   :total_students_attempting: 50
   :num_students_correct: 27.0
   :mean_clicks_to_correct: 4.3333333333

   Create a while loop that randomly generates numbers until the sum of the numbers ``sum_rand`` is greater than 100. Create a histogram using Altair with all the random numbers found. 
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertTrue(sum_rand>100,"The sum of the random numbers is greater than 100")
           self.assertIn('import altair', self.getEditorText(), 'Contains altair')
           self.assertIn('while', self.getEditorText(), 'Contains while')
           self.assertIn('import random', self.getEditorText(), 'Contains random')
   
   
           
   myTests().main()