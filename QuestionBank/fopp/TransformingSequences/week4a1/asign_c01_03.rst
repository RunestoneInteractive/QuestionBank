.. activecode:: asign_c01_03
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

   Write code that uses the string stored in ``sent`` and creates an acronym which is assigned to the variable ``acro``. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a ". " (dot and space). Words that should not be included in the acronym are stored in the list ``stopwords``. For example, if ``sent`` was assigned the string "height and ewok wonder" then the resulting acronym should be "HE. EW. WO".
   ~~~~
   stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
   sent = "The water earth and air are vital"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(acro, 'WA. EA. AI. AR. VI', 'Checking that acro has been set correctly.')
         self.assertTrue(type(acro) == type("string"), "Checking that acro is a string.")
         self.assertIn('for', self.getEditorText(), "Testing that you used a for loop.")

   myTests().main()