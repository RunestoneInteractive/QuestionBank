.. actex:: ex_7_9_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 15
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 26.0

   Write a function, ``is_prime``, that takes a single integer argument
   and returns ``True`` when the argument is a *prime number* and ``False``
   otherwise.
   ~~~~
   
   def is_prime(n):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(2, len(re.findall("\s*return", editText)), "Need two return statements")
           self.assertEqual(is_prime(2),True,"Tested on 2, which is a prime number.")
           self.assertEqual(is_prime(4187),False,"Tested on 4187, which is not a prime number. It is divisible by 53 and 79.")
           self.assertEqual(is_prime(22),False,"Tested on 22, which is not a prime number. It is divisible by 2 and 11.")
           self.assertEqual(is_prime(4813),True,"Tested on 4813, which is a prime number.")
           self.assertEqual(is_prime(1),False,"Tested on 1 which is not a prime number.")
           
   myTests().main()