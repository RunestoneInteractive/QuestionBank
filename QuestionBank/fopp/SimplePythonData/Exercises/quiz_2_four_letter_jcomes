.. actex:: quiz_2_four_letter_jcomes
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest

   Write a program that does the following: (1) prompts the user for a four letter word, 
   (2) stores the word provided by the user in a variable called ``word``, and then 
   (3) prints a message to the user telling them how many characters are in the word.
   
   For example, if the user enters the word ``quiz``, the program should tell them there are 4 
   characters. If the user enters ``I can't``, the program should tell them there are 7 characters (counting the apostrophe and the space).
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
           self.assertEqual(type(word), type('Pat'), 'Checking for the variable name')
           self.assertTrue(re.search(str(len(word)), self.getOutput()), 'Checking answer.')
   myTests().main()