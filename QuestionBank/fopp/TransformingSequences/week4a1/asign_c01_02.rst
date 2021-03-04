.. activecode:: asign_c01_02
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

   Write code that uses the string stored in ``org`` and creates an acronym which is assigned to the variable ``acro``. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list ``stopwords``. For example, if ``org`` was assigned the string "hello to world" then the resulting acronym should be "HW".
   ~~~~
   stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
   org = "The organization for health, safety, and education"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(acro, 'OHSE', 'Checking that acro has been set correctly.')
         self.assertTrue(type(acro) == type("string"), "Checking that acro is a string.")
         self.assertIn('for', self.getEditorText(), "Testing that you used a for loop.")

   myTests().main()