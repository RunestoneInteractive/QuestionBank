.. activecode:: final_exam_4
   :author: Irma Ravkic
   :difficulty: 1.1178045515
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.14
   :total_students_attempting: 50
   :num_students_correct: 20.0
   :mean_clicks_to_correct: 3.0

   
   Write a program that will create a dictionary called ``my_dictionary`` out of the list of strings below where the keys are each word from the list, and the values are the counts of how many times each word occurs in the list. Your result should be the following dictionary:
   
   "":2 
   
   "hello": 2
   
   "goodbye": 2
   
   "I love Python": 1
   
   "wonderful": 1
   
   (You might get a different order of elements)
   ~~~~
   my_list = ["","hello","", "goodbye", "wonderful", "hello", "goodbye", "I love Python"]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def test_output(self):
           self.assertIn('for', self.getEditorText(), "You should be using a for loop.")
           self.assertIn('my_dictionary', self.getEditorText(), "Use my_dictionary variable.")
       def testTwo(self):
           self.assertEqual(my_dictionary[""], 2, 'Checking the count for the empty string ""')
           self.assertEqual(my_dictionary["hello"], 2, 'Checking the count for hello')
           self.assertEqual(my_dictionary["goodbye"], 2, 'Checking the count for goodbye')
           self.assertEqual(my_dictionary["I love Python"], 1, 'Checking the count for I love Python')
           self.assertEqual(my_dictionary["wonderful"], 1, 'Checking the count for wonderful')
           self.assertEqual(len(my_dictionary), 5, 'The length of your dictionary')
   
   
   
   myTests().main()