.. activecode:: hill2019-easydictionary
   :author: Scott Hill
   :difficulty: 1.2524383247
   :basecourse: fopp
   :chapter: TestCases
   :subchapter: Exercises
   :topics: TestCases/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :language: python
   :nopair: 
   :pct_on_first: 0.2222222222
   :total_students_attempting: 9
   :num_students_correct: 7.0
   :mean_clicks_to_correct: 5.2857142857

   A dictionary of prices is defined below. Write some code that uses the dictionary to find and print out the total price of an apple and a banana.  Do *not* hard-code your answer.
   
   ~~~~
   #Enter code here
   prices={'apple':0.75,'banana':0.30,'orange':0.50,'watermelon':2.00} 
   
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):           
   
        def testOne(self):
            self.assertTrue(('0.75+0.30' not in self.getEditorText().replace(" ","")) and ('1.05' not in self.getEditorText()),"Did you hard-code?")
            self.assertTrue('prices["apple"]' in self.getEditorText().replace("'",'"'),"Did you use the dictionary?")
            self.assertTrue('1.05' in self.getOutput(),"Is the answer right?")
        
   
   myTests().main()