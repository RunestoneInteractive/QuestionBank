.. activecode:: KDL_ch8_2
   :author: Kaelyn Leake
   :difficulty: 1.1423471664
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.3333333333
   :total_students_attempting: 12
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 3.4166666667

   A grading scheme is provided::
   
      A 90<x<=100
      B 80<x<=90
      C 70<x<=80
      D 60<x<=70
      F 0<x<=60
   
   Use an if statement to determine the correct ``letter_grade`` based on the ``percentage`` someone has in class. Print the letter grade.
   
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           if percentage>90:
              letters_grade='A'
           elif percentage>80:
              letters_grade='B'
           elif percentage>70:
              letters_grade='C'
           elif percentage>60:
              letters_grade='D'
           else:
              letters_grade='F'
   
           self.assertTrue(letters_grade==letter_grade[::-1],feedback="Letter grade correct")
           self.assertIn('if ', self.getEditorText(), 'Contains if statement')
           self.assertIn('print(', self.getEditorText(), 'Contains print in if statement')
           
   myTests().main()