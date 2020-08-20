.. activecode:: question9_1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionaries1
   :topics: 09-dictionaries/09-dictionaries1
   :from_source: T
   :practice: T
   :nocodelens:

   Write code that adds the key 'two' with a value of 'dos' to the dictionary eng2sp.
   ~~~~
   eng2sp = {'one':'uno'}

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(eng2sp['two'], 'dos', "Testing if the key 'two' maps to 'dos'.")

   myTests().main()