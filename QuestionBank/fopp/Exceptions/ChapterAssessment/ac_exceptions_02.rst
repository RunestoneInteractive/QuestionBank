.. activecode:: ac_exceptions_02
   :author: bmiller
   :difficulty: 1.0808462609
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: ChapterAssessment
   :topics: Exceptions/ChapterAssessment
   :from_source: T
   :tags:Exceptions/intro-exceptions.rst: 
   :pct_on_first: 0.359375
   :total_students_attempting: 128
   :num_students_correct: 102.0
   :mean_clicks_to_correct: 2.3725490196

   The list, ``numb``, contains integers. Write code that populates the list ``remainder`` with the remainder of 36 divided by each number in ``numb``. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string "Error" appear in the ``remainder``.
   ~~~~
   
   numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
   
   remainder = []
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOneA(self):
         self.assertEqual(remainder, [0, 'Error', 0, 4, 0, 0, 'Error', 0, 36, 'Error', 36, 'Error', 0, 13], "Testing that remainder is assigned to correct values.")
   
   myTests().main()