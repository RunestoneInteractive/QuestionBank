.. actex:: rab_lq4_ex2
   :author: Richard Bernatz
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.0681818182
   :total_students_attempting: 44
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 8.75

   Use this active code window for coding problem 2. Include the required function only!
    
    
   ~~~~
   # your name
   def pair_names(f_names, l_names, first):
    
    
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           fn = ['Mary', 'Roberto', 'Ed', 'Al']
           ln = ['Jones', 'Suarez', 'Hicks', 'Lund']
           self.assertEqual(pair_names(fn,ln,True), ['Mary Jones', 'Roberto Suarez', 'Ed Hicks', 'Al Lund'])
           self.assertEqual(pair_names(fn,ln,False), [['Jones', 'Mary'], ['Suarez', 'Roberto'], ['Hicks', 'Ed'], ['Lund', 'Al']])
           
          
   myTests().main()