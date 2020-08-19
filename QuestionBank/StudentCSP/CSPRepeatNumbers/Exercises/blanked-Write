.. activecode:: blanked-Write
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: Exercises
   :topics: CSPRepeatNumbers/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.1294117647
   :total_students_attempting: 255
   :num_students_correct: 235.0
   :mean_clicks_to_correct: 9.5361702128

   Define the function blanked().  It takes a word and a string of letters that have been revealed.
   It should return a string with the same number of characters as
   the original word, but with the unrevealed characters replaced by _
   ~~~~
   def blanked(word, revealed_letters):
       return word
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(blanked('hello', 'elj'), "_ell_", "testing blanking of hello when e,l, and j have been guessed.")
           self.assertEqual(blanked('hello', ''), '_____', "testing blanking of hello when nothing has been guessed.")
           self.assertEqual(blanked('ground', 'rn'), '_r__n_', "testing blanking of ground when r and n have been guessed.")
           self.assertEqual(blanked('almost', 'vrnalmqpost'), 'almost', "testing blanking of almost when all the letters have been guessed.")
   
   myTests().main()