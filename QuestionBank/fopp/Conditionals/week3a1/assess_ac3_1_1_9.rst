.. activecode:: assess_ac3_1_1_9
   :author: bmiller
   :difficulty: 1.0475938255
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: week3a1
   :topics: Conditionals/week3a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6045576408
   :total_students_attempting: 746
   :num_students_correct: 599.0
   :mean_clicks_to_correct: 1.8080133556

   Create the variable ``z`` whose value is ``30``. Write code to see if ``z`` is greater than ``y``. If so, add 5 to ``y``'s value, otherwise do nothing. Then, multiply ``z`` and ``y``, and assign the resulting value to the variable ``x``.
   ~~~~
   y = 22
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(x, 810, "Testing the value of x")
      def testTwo(self):
         self.assertEqual(z, 30, "Testing the value of z.")
   
   myTests().main()