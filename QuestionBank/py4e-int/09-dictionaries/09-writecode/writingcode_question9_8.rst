.. activecode:: writingcode_question9_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
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
           self.assertEqual(eng2sp['two'], 'dos', "Making sure the correct value is associated with the key 'two'.")

   myTests().main()