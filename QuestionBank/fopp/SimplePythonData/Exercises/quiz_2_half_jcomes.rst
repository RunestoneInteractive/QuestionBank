.. actex:: quiz_2_half_jcomes
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest

   Write a program that (1) prompts the user for a number, (2) stores their 
   input as type ``float`` in a variable called ``num``, then (3) prints a message telling the user what half of the number is.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
           self.assertEqual(type(num), type(2.3), 'Checking the type of the variable age')
           self.assertTrue(re.search(str(num / 2)[:5], self.getOutput()), 'Checking answer.')
   myTests().main()