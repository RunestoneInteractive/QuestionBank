.. activecode:: assess_ps_02_09
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: week2a2
   :topics: Iteration/week2a2
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T

   Write code to create a list of numbers from 0 to 67 and assign that list to the variable ``nums``. Do not hard code the list.
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(nums, range(68), "Testing that nums is a list that contains the correct elements.")

   myTests().main()