.. activecode:: assess_pc_02_10
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

   Create an empty string and assign it to the variable ``lett``. Then using range, write code such that when your code is run, ``lett`` has 7 b's (``"bbbbbbb"``).
   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lett, "bbbbbbb", "Testing that lett has the correct value." )
         self.assertNotIn("bbbbbbb", self.getEditorText(), "Testing that you didn't hardcode the answer.")

   myTests().main()