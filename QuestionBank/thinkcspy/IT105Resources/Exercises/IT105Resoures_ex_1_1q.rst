.. actex:: IT105Resoures_ex_1_1q
   :author: jenkins
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: IT105Resources
   :subchapter: Exercises
   :topics: IT105Resources/Exercises
   :from_source: F
   :pct_on_first: 0.5833333333
   :total_students_attempting: 12
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 1.5

   Write a function to count how many even numbers are in a list.
   ~~~~
   def countEven(lst):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(countEven([1,3,5,7,9]),0,"Tested countEven on input [1,3,5,7,9]")
           self.assertEqual(countEven([1,2,3,4,5]),2,"Tested countEven on input [1,2,3,4,5]")
           self.assertEqual(countEven([2,4,6,8,10]),5,"Tested countEven on input [2,4,6,8,10]")
           self.assertEqual(countEven([0,-1,12,-33]),2,"Tested countEven on input [0,-1,12,-33]")
   
   myTests().main()