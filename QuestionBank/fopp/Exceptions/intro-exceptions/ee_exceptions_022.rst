.. activecode:: ee_exceptions_022
   :author: bmiller
   :difficulty: 1.0692021273
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: intro-exceptions
   :topics: Exceptions/intro-exceptions
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :pct_on_first: 0.5
   :total_students_attempting: 196
   :num_students_correct: 183.0
   :mean_clicks_to_correct: 2.174863388

   6. Below, we have provided code that does not run. Add a try/except clause so the code runs without errors. If an element is not able to undergo the addition operation, the string 'Error' should be appended to plus_four.
   ~~~~
   
   nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]
   
   plus_four = []
   
   for num in nums:
       plus_four.append(num+4)
   
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(plus_four, [9, 13, 'Error', 7, 6, 5, 10, 9, 'Error', 8, 7, 6, 10, 11, 12, 'Error', 7, 8, 4, 10, 9, 'Error', 9, 10, 11, 12, 'Error', 'Error', 9, 10, 11, 13, 7, 6, 9, 10, 'Error', 6, 7, 8, 9, 5], "Testing that plus_four is created correctly.")
   
   myTests().main()