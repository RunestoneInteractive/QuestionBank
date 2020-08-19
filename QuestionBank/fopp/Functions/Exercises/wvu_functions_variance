.. activecode:: wvu_functions_variance
   :author: Brian Powell
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.1176470588
   :total_students_attempting: 34
   :num_students_correct: 16.0
   :mean_clicks_to_correct: 5.25

   Variance can be calculated as **(∑(x−x̄)²)/n**, where **x̄** is the average of all **x** and **n** is the count of how many **x** there are.
   
   Standard deviation is the square root of variance.
   
   Write a function named **variance** that will return the variance of a list. Write a second function named **stdev** that will return the standard deviation of a list.
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(round(variance([1,3,5]),3),2.667,"Your code must calculate the variance using the provided formula")
      def testStdev(self):
         self.assertEqual(round(stdev([1,3,5]),3),1.633,"Your code must calculate the standard deviation using the provided formula")
   myTests().main()