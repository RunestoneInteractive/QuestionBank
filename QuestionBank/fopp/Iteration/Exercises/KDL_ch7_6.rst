.. activecode:: KDL_ch7_6
   :author: Kaelyn Leake
   :difficulty: 1.0589022758
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.5384615385
   :total_students_attempting: 13
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 2.0

   Turn this list of strings into a single string called ``strg``. Use a for loop to do so. Print the string.
   ~~~~
   list_of_strings=["This ","is a ","string","made","from","a list"]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           a=""
           for stringv in list_of_strings:
               a=a+stringv
           self.assertIn(str(a)[:10], self.getOutput(), 'Checking sentence.')
           self.assertTrue(strg==a,feedback="names is long enough")
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
   myTests().main()