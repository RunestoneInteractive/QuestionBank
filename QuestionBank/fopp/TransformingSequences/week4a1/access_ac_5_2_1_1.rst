.. activecode:: access_ac_5_2_1_1
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

   For each character in the string saved in ``ael``, append that character to a list that should be saved in a variable ``app``.
   ~~~~
   ael = "python!"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(app, ['p','y','t','h','o','n', "!"], "Testing that app has the correct elements." )
         self.assertIn('append', self.getEditorText(), "Testing that your code uses append.")

   myTests().main()