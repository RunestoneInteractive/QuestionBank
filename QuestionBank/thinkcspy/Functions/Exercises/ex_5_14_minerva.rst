.. actex:: ex_5_14_minerva
   :author: Svitlana Midianko
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 0.4444444444
   :total_students_attempting: 18
   :num_students_correct: 15.0
   :mean_clicks_to_correct: 6.1333333333

   **# # # EXTRA QUESTIONS # # #**
   Write a function called ``mySqrt`` that will approximate the square root of a number, call it n, by using
   Newton's algorithm.
   Newton's approach is an iterative guessing algorithm where the initial guess is n/2 and each subsequent guess
   is computed using   the formula:  newguess = (1/2) * (oldguess + (n/oldguess)).
   ~~~~
   
   def mySqrt(n):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertAlmostEqual(mySqrt(4.0),2.0,0,"Tested mySqrt on input 4.0")
           self.assertAlmostEqual(mySqrt(9.0),3.0,4,"Tested accuracy of mySqrt on input 3.0")
           self.assertAlmostEqual(mySqrt(36.0),6.0,5,"Tested accuracy of mySqrt on input 6.0")
           self.assertAlmostEqual(mySqrt(100.0),10.0,4,"Tested accuracy of mySqrt on input 10.0. Try iterating more times.")
   
   myTests().main()