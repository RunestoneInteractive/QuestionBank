.. activecode:: ac3_8_7_jcomes
   :author: Jonny Comes
   :difficulty: 1.0147255689
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.3
   :total_students_attempting: 10
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 1.25

   Create a turtle and assign it to a variable. Print the type of your turtle and see what you get.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
   
           answer = str(type(turtle.Turtle()))
           self.assertTrue(re.search(answer, self.getOutput()), 'Checking answer.')
   
   
           
   myTests().main()