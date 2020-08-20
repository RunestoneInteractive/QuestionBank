.. activecode:: KDL_ch11_1
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0955414013
   :total_students_attempting: 157
   :num_students_correct: 83.0
   :mean_clicks_to_correct: 8.156626506

   Create a function ``lower_upper_count`` that accepts a string and returns a dictionary that contains the count for upper and lower case characters in that string. For example "Sweet Briar" should get {'lower': 8, 'upper': 2}. I suggest removing spaces first...
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('def lower_upper_count', self.getEditorText(), 'Contains correctly named function')
           self.assertEqual(lower_upper_count(''),{'lower': 0, 'upper': 0},"the correct count for ''")
           self.assertEqual(lower_upper_count('This String Has MANY upper and LOWER case letters'),{'lower': 29, 'upper': 12},"the correct count for 'This String Has MANY upper and LOWER case letters'")
   
           
   myTests().main()