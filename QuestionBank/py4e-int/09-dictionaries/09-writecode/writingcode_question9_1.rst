.. activecode:: writingcode_question9_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   Write a program that reads the words in the string 'phrase' and counts how many times each word appears.
   Store the words as keys in the dictionary 'word_dictionary', then use the ``in`` operator as a fast way to
   check whether the string is in the dictionary.
   ~~~~

   phrase = "Writing programs or programming is a very creative and rewarding activity  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem  This book assumes that {\em everyone} needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(len(word_dictionary), 56, "Checking that all the words made it into the list.")
           self.assertEqual(word_dictionary['Writing'], 1, "Checking that 'Writing' appears once in the dictionary.")
           self.assertEqual(word_dictionary['a'], 3, "Making sure the letter 'a' appears three times as a word in the given phrase.")

   myTests().main()