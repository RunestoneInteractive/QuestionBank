.. actex:: ex_7_10_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Write a function that will return the number of digits in an integer.
   ~~~~
   def numDigits(n):
       # your code here
   
   ====
   
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
           self.assertEqual(numDigits(2),1,"Tested numDigits on input of 2")
           self.assertEqual(numDigits(55),2,"Tested numDigits on input of 55")
           self.assertEqual(numDigits(1352),4,"Tested numDigits on input of 1352")
           self.assertEqual(numDigits(444),3,"Tested numDigits on input of 444")
           self.assertEqual(numDigits(0),1,"Tested numDigits on input of 0")
   
   
   
   myTests().main()