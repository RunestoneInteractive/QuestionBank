.. actex:: ex_6_12_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   3 criteria must be taken into account to identify leap years:
   
   The year is evenly divisible by 4;
   
   If the year can be evenly divided by 100, it is NOT a leap year, unless;
   
   The year is also evenly divisible by 400. Then it is a leap year.
   
   Write a function that takes a year as a parameter and returns ``True`` if the year is a leap year, ``False`` otherwise.
   ~~~~
   def isLeap(year):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
           self.assertEqual(isLeap(1944),True,"Tested isLeap on an input of 1944")
           self.assertEqual(isLeap(2011),False,"Tested isLeap on an input of 2011")
           self.assertEqual(isLeap(1986),False,"Tested isLeap on an input of 1986")
           self.assertEqual(isLeap(1800),False,"Tested isLeap on an input of 1800")
           self.assertEqual(isLeap(1900),False,"Tested isLeap on an input of 1900")
           self.assertEqual(isLeap(2000),True,"Tested isLeap on an input of 2000")
           self.assertEqual(isLeap(2056),True,"Tested isLeap on an input of 2056")
           self.assertEqual(isLeap(4),True,"Tested isLeap on an input of 4")
           self.assertEqual(isLeap(100),False,"Tested isLeap on an input of 100")
   
   myTests().main()