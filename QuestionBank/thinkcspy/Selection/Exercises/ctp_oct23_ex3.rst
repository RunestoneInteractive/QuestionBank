.. actex:: ctp_oct23_ex3
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F
   :pct_on_first: 0.0505050505
   :total_students_attempting: 99
   :num_students_correct: 32.0
   :mean_clicks_to_correct: 14.84375

   [30 pts] Write a function ``isLeap`` that takes as argument an integer representing a given year.  The function should return ``True`` if the year is a leap year, ``False`` otherwise.  In doing so, 3 criteria must be taken into account to identify leap years:
   
   The year is evenly divisible by 4;
   
   If the year can be evenly divided by 100, it is NOT a leap year, unless;
   
   The year is also evenly divisible by 400. Then it is a leap year.
   
   To test your function, write a program that asks the user for the year, calls your function, and prints the returned value.
   ~~~~
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(isLeap(1944),True,"Tested isLeap on an input of 1944")
           self.assertEqual(isLeap(2011),False,"Tested isLeap on an input of 2011")
           self.assertEqual(isLeap(1986),False,"Tested isLeap on an input of 1986")
           self.assertEqual(isLeap(1800),False,"Tested isLeap on an input of 1800")
           self.assertEqual(isLeap(1900),False,"Tested isLeap on an input of 1900")
           self.assertEqual(isLeap(2000),True,"Tested isLeap on an input of 2000")
           self.assertEqual(isLeap(2056),True,"Tested isLeap on an input of 2056")
   
   myTests().main()