.. actex:: rab_hw_ex_03_ch_10
   :author: Richard Bernatz
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.14
   :total_students_attempting: 100
   :num_students_correct: 90.0
   :mean_clicks_to_correct: 11.9444444444

   Write a function called ```change_tuple(t_in, kind, item, spot)``` that makes a change to tuple and returns the new tuple. The parameter ```t_in``` is the tuple, parameter ```kind``` is a string with value either 'add' or 'replace', parameter ```item``` is the value of the item that will either be added to the tuple at the end, or replace the current value of the tuple in the location specified by the optional parameter ```spot```. NOTE: The optional parameter ```spot``` is defaulted to 0 if no value is included in the call to the function. If the value of ```kind``` is not one of 'add' or 'replace,' then ```t_in``` is returned unchanged.
   
   
   ~~~~
   def change_tuple(t_in, kind, item, spot=0):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           t_in = ('James', 'Smith', 42, 'Decorah', 'Iowa')
           t_out = change_tuple(t_in, 'add', 'farmer')
           self.assertEqual(t_out, ('James', 'Smith', 42, 'Decorah', 'Iowa', 'farmer'),"Tested change_tuple(t_in, 'add', 'farmer')")
           t_in = ('James', 'Smith', 42, 'Decorah', 'Iowa')
           t_out = change_tuple(t_in, 'replace', 43, 2)
           self.assertEqual(t_out, ('James', 'Smith', 43, 'Decorah', 'Iowa'), "Tested change_tuple(t_in, 'replace', 43, 2) ")  
           t_in = ('James', 'Smith', 42, 'Decorah', 'Iowa')
           t_out = change_tuple(t_in, 'replace', 'Jim', 0)
           self.assertEqual(t_out, ('Jim', 'Smith', 42, 'Decorah', 'Iowa'), "Tested change_tuple(t_in, 'replace', 'Jim', 0)")
           t_in = ('James', 'Smith', 42, 'Decorah', 'Iowa')
           t_out = change_tuple(t_in, 'change', 'Iowa City', 3)
           self.assertEqual(t_out, ('James', 'Smith', 42, 'Decorah', 'Iowa'), "Tested change_tuple(t_in, 'change', 'Iowa City', 3)")    
           t_in = ('James', 'Smith', 42, 'Decorah', 'Iowa')
           t_out = change_tuple(t_in, 'replace', 'Iowa City', 3)
           self.assertEqual(t_out, ('James', 'Smith', 42, 'Iowa City', 'Iowa'), "Tested change_tuple(t_in, 'replace', 'Iowa City', 3)")            
          
   myTests().main()