.. activecode:: ac_exceptions_03
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: ChapterAssessment
   :topics: Exceptions/ChapterAssessment
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :practice: T

   Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list ``attempt`` the string "Error".
   ~~~~

   full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

   attempt = []

   for elem in full_lst:
       attempt.append(elem[1])

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(attempt, ['b', 'd', 'g', 'Error', 'k', 'o', 'r', 'Error', 'v', 'x', 'Error'], "Testing that attempt has the correct values.")

   myTests().main()