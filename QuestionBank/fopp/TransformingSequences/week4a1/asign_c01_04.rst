.. activecode:: asign_c01_04
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

   A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if ``p_phrase`` is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of ``p_phrase`` to the variable ``r_phrase`` so that we can check your work.
   ~~~~
   p_phrase = "was it a car or a cat I saw"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(r_phrase, "was I tac a ro rac a ti saw", "checking that r_phrase is set correctly")
         stripped_phrase = p_phrase.replace(" ", "").lower()
         stripped_r_phrase = r_phrase.replace(" ", "").lower()
         self.assertEqual(stripped_phrase, stripped_r_phrase, "checking that r_phrase and p_phrase are equivalent if the spaces are placed in the correct locations.")
         self.assertIsNot(p_phrase, r_phrase, "checking that r_phrase and p_phrase are not the same object.")

   myTests().main()