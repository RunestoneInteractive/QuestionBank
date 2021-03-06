.. activecode:: ac_exceptions_04
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: ChapterAssessment
   :topics: Exceptions/ChapterAssessment
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :practice: T

   The buggy code below prints out the value of the sport in the list ``sport``. Use try/except so that the code will run properly. If the sport is not in the dictionary, ``ppl_play``, add it in with the value of 1.
   ~~~~

   sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

   ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

   for x in sport:

        print(ppl_play[x])

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(sorted(ppl_play.items()), [('baseball', 1), ('basketball', 1), ('football', 15), ('hockey', 4), ('soccer', 10), ('tennis', 8)], "Testing that ppl_play is assigned to correct values.")

   myTests().main()