.. actex:: ex_5_14_rab
   :author: Richard Bernatz
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :pct_on_first: 0.1063829787
   :total_students_attempting: 47
   :num_students_correct: 43.0
   :mean_clicks_to_correct: 11.6744186047

   Write a function called ``my_sqrt`` that will approximate the square root of a number, call it n, by using
   Newton's algorithm.
   Newton's approach is an iterative guessing algorithm where the initial guess is n/2 and each subsequent guess
   is computed using   the formula:  newguess = (1/2) * (oldguess + (n/oldguess)). Begin by using 4 iterations.
   ~~~~
   
   def my_sqrt(n):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertAlmostEqual(my_sqrt(4.0),2.0,0,"Tested my_sqrt on input 4.0")
           self.assertAlmostEqual(my_sqrt(9.0),3.0,4,"Tested accuracy of my_sqrt on input 9.0")
           self.assertAlmostEqual(my_sqrt(36.0),6.0,5,"Tested accuracy of my_sqrt on input 36.0")
           self.assertAlmostEqual(my_sqrt(100.0),10.0,6,"Tested accuracy of my_sqrt on input 100.0. Try iterating more times.")
   
   myTests().main()