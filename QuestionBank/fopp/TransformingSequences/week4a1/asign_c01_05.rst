.. activecode:: asign_c01_05
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T

   Provided is a list of data about a store's inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read ``The store has 12 shoes, each for 29.99 USD.``
   ~~~~
   inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
          self.assertIn('for', self.getEditorText(), "Testing whether your code includes a for loop.")
          self.assertIn('.format(', self.getEditorText(), "Testing whether your code invokes the .format method.")
          self.assertIn('The store has 12 shoes, each for 29.99 USD.\nThe store has 20 shirts, each for 9.99 USD.\nThe store has 25 sweatpants, each for 15.00 USD.\nThe store has 13 scarves, each for 7.75 USD.\n', self.getOutput(), "Testing your output.")



   myTests().main()