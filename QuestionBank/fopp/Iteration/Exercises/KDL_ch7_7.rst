.. activecode:: KDL_ch7_7
   :author: Kaelyn Leake
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.2857142857
   :total_students_attempting: 14
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 9.9166666667

   Using a user input create a string ``s``. Split the string into a list of letters ``l`` using a for loop. For example s='The cat" would get l=['T','h','e',' ','c','a','t'] 
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           def split(s):
               t=[]
               for letter in s:
                    t+=[letter]
               return t
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           self.assertIn('input(', self.getEditorText(), 'Contains input')
           self.assertEqual(split(s), l, "testing list.")
           
   myTests().main()