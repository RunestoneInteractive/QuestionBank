.. activecode:: writingcode_question9_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :nocodelens:

   Perform the same task as in question 1, but this time make sure to look at words in lowercase in order to avoid any repetition.
   ~~~~

   phrase = "Writing programs or programming is a very creative and rewarding activity  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem  This book assumes that {\em everyone} needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(len(word_dictionary), 55, "Checking that all the terms were accounted for in the new list.")
           self.assertEqual(word_dictionary['you'], 4, "Checking the amount of times 'you' appears in the phrase.")
           self.assertEqual(word_dictionary['writing'], 1, "Making sure 'writing' appears just once in the dictionary.")
           self.assertEqual(word_dictionary.get('Writing', 0), 0, "Checking to make sure 'Writing' is no longer in the dictionary.")

   myTests().main()