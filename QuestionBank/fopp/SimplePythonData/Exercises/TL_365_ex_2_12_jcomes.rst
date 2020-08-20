.. actex:: TL_365_ex_2_12_jcomes
   :author: Jonny Comes
   :difficulty: 1.0706827309
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.6666666667
   :total_students_attempting: 6
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 2.2

   Write a program that will compute MPG for a car. Prompt the user to
   enter the number of miles driven and the number of gallons
   used. Store the values as type ``float`` in variables call ``miles``
   and ``gallons`` respectively. Print a nice message with the answer.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
           self.assertEqual(type(miles), type(2.2), 'Checking the type of the variable miles')
           self.assertEqual(type(gallons), type(2.2), 'Checking the type of the variable gallons')
           self.assertTrue(re.search(str(miles/gallons)[:5], self.getOutput()), 'Checking answer.')
   myTests().main()