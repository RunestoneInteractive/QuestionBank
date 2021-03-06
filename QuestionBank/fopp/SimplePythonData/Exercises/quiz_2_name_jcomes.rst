.. actex:: quiz_2_name_jcomes
   :author: Jonny Comes
   :difficulty: 1.0147255689
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 6
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 1.25

   Write a program that does the following: (1) prompts the user for a name, 
   (2) stores the name provided by the user in a variable called ``name``, and then 
   (3) prints a message to the user telling them how many characters are in the name.
   
   For example, if the user enters the name ``Jonny``, the program should tell them there are 5 
   characters in that name. If the user enters ``Dr. Danielson``, the program should tell them there are 13 characters (counting the period and the space).
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
           self.assertEqual(type(name), type('Pat'), 'Checking for the variable name')
           self.assertTrue(re.search(str(len(name)), self.getOutput()), 'Checking answer.')
   myTests().main()