.. activecode:: KDL_ch7_8
   :author: Kaelyn Leake
   :difficulty: 1.1816153503
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1470588235
   :total_students_attempting: 68
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 4.0833333333

   Ask the user for a integer ``i``. Use a for loop to find i*i*i*i (aka :math:`{i}^{4}`) and save this to the variable ``g``.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue('for ' in self.getEditorText(), 'Contains for loop')
           self.assertTrue('input(' in self.getEditorText(), 'Contains input')
           self.assertTrue('i*i*i*i' not in self.getEditorText(), "Checking for hardcoding")
           self.assertTrue('i**4' not in self.getEditorText(), "Checking for hardcoding")
           self.assertTrue('i*i*i*i' not in self.getEditorText(), "Checking for hardcoding")
           self.assertTrue(g==(int(i))**4, "Checking for correct answer")
   myTests().main()