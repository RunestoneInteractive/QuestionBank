.. actex:: rab_lq4_ex1
   :author: Richard Bernatz
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.0425531915
   :total_students_attempting: 47
   :num_students_correct: 26.0
   :mean_clicks_to_correct: 19.3846153846

   Use this active code window for coding problem 1. Include the required function only!
    
    
   ~~~~
   # your name
   def decipher_word(w_in):
    
    
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(decipher_word('OM3nn2s4t1$'), 'Minnesota', "Tested OM3nn2s4t1$ == Minnesota")
           self.assertEqual(decipher_word('(5mbr2ll1E'), 'umbrella', "Tested (5mbr2ll1E == umbrella")
           self.assertEqual(decipher_word('FMcD45g1llj'), 'McDougall', "Tested FMcD45g1llj == McDougall")
           self.assertEqual(decipher_word('ixyl4ph4n2J'), 'xylophone', "Tested ixyl4ph4n2J == xylophone")
           self.assertEqual(decipher_word('^W1ps3p3n3c4nb'), 'Wapsipinicon', "Tested ^W1ps3p3n3c4nb == Wapsipinicon")
           
          
   myTests().main()