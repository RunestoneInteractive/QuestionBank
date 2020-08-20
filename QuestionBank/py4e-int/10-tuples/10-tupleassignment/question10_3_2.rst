.. activecode:: question10_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-tupleassignment
   :topics: 10-tuples/10-tupleassignment
   :from_source: T
   :nocodelens:
   :practice: T

   Write code to swap the values of tuple t.
   ~~~~
   t = ('Antetokounmpo', 'Giannis')

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(t, ('Giannis', 'Antetokounmpo'), "Checking that the two values of the tuple were swapped.")

   myTests().main()