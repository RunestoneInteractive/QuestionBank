.. activecode:: wvu_functions_oddlist
   :author: Brian Powell
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Write a function named **generate_odd_numbers** that will generate a list containing every odd number between 0 and a number specified by the user, excluding the user-specified number. The function must return the generated list.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(len(generate_odd_numbers(6)),3,"Your code must generate a list of odd numbers")
   myTests().main()