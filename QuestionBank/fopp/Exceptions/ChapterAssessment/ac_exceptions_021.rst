.. activecode:: ac_exceptions_021
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: ChapterAssessment
   :topics: Exceptions/ChapterAssessment
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :practice: T

   Provided is buggy code, insert a try/except so that the code passes.
   ~~~~

   lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

   lst_three = []

   for num in lst:
       if 3 % num == 0:
           lst_three.append(num)


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(lst_three, [1,3], "Testing that lst_three has the correct values.")

   myTests().main()