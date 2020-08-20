.. activecode:: writingcode_question10_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(updated_list, [(10, 20, 100), (40, 50, 100), (70, 80, 100)], "Testing to make sure the last value of each tuple is 100.")

   MyTests().main()