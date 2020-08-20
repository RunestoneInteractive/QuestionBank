.. activecode:: KDL_ch9_2
   :author: Kaelyn Leake
   :difficulty: 1.4588898229
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0597014925
   :total_students_attempting: 67
   :num_students_correct: 43.0
   :mean_clicks_to_correct: 8.7906976744

   Write a function ``lettercount`` that accepts a list and a letter. The function should return a new list with all the words in the original list that have the letter in them with a dash and the number of times that letter is in the word. For example lettercount(['cat','dog','parakeet','turtle'],'t') should return ['cat-1','parakeet-1','turtle-2']. Use append to add to your list.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           def _lettercount(list,letter):
                new_list=[]
                for word in list:
                   lc=word.count(letter)
                   if lc>0:
                       wordcount=word+'-'+str(lc)
                       new_list.append(wordcount)
                return new_list
           t_list=['this','list', 'is', 'totally', 'super','scrumptious']
           self.assertIn('def lettercount', self.getEditorText(), 'Contains lettercount function')
           self.assertIn('append(', self.getEditorText(), 'Contains append')
           self.assertEqual(_lettercount(t_list,'s'), lettercount(t_list,'s'), "Result of lettercount correct")
           
   myTests().main()