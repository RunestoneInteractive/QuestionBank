.. activecode:: assess_week5_01
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T

   Currently there is a string called ``str1``. Write code to create a list called ``chars`` which should contain the characters from ``str1``. Each character in ``str1`` should be its own element in the list ``chars``.
   ~~~~
   str1 = "I love python"
   # HINT: what's the accumulator? That should go here.

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(chars, ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n'], "Testing that chars is assigned the correct value.")

   myTests().main()