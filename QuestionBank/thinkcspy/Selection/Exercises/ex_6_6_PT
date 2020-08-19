.. actex:: ex_6_6_PT
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
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Write a function ``findHypot``.  The function will be given the length of two sides of a right-angled triangle and it should return
   the length of the hypotenuse.  (Hint:  ``x ** 0.5`` will return the square root, or use ``sqrt`` from the math module)
   ~~~~
   
   def findHypot(a,b):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
           self.assertEqual(findHypot(4,3),5.0,"Tested findHypot on inputs of 4 and 3")
           self.assertEqual(findHypot(3,4),5.0,"Tested findHypot on inputs of 3 and 4")
           self.assertEqual(findHypot(12.0,5.0),13.0,"Tested findHypot on inputs of 12.0 and 5.0")
           self.assertEqual(findHypot(0.4,0.3),0.5,"Tested findHypot on inputs of 0.4 and 0.3")
           
          
   
           
   
   myTests().main()