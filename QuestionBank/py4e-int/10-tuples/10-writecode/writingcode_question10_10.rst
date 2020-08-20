.. activecode:: writingcode_question10_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :nocodelens:
   :practice: T

   Create a function tuplize that accepts two inputs and returns them in a tuple. The first input and then the second.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(tuplize('Stephen', 'Curry'), ('Stephen', 'Curry'), "Testing that the function creates the correct tuple.")

   MyTests().main()