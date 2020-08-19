.. actex:: quiz_2_age_jcomes
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 8
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.2

   Write a program that (1) prompts the user for their age in years, (2) stores their 
   input as type ``int`` in a variable called ``age``, then (3) prints a message saying how old they will be 5 years from now.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
           self.assertEqual(type(age), type(2), 'Checking the type of the variable age')
           self.assertTrue(re.search(str(age + 5), self.getOutput()), 'Checking answer.')
   myTests().main()