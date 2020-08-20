.. activecode:: wvu_functions_listaverage
   :author: Brian Powell
   :difficulty: 1.1737617135
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.1153846154
   :total_students_attempting: 52
   :num_students_correct: 20.0
   :mean_clicks_to_correct: 3.95

   Write a function named **average_odd_list** that will return the average of the odd numbers between 0 and a number specified by the user, excluding the user-specified number. The function must return the average.
   
   The **average_odd_list** function must make use of the **generate_odd_numbers** function from the wvu_functions_createlist question. You may copy-and-paste the source code for that function here.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(len(generate_odd_numbers(6)),3,"Your code must generate a list of odd numbers")
         self.assertEqual(average_odd_list(6),3,"Your average_odd_list function must return the average of the odd number values")
   myTests().main()