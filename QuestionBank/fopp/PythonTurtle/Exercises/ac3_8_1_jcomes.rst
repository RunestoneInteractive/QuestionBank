.. actex:: ac3_8_1_jcomes
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 10
   :num_students_correct: 10.0
   :mean_clicks_to_correct: 2.9

   Write a program that prints ``We like Python's turtles!`` 100 times.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn("We like Python's turtles!", self.getEditorText(), 'Checking the message appears in the code.\nNote: Capitalization, punctuation, and spacing matter!')
           self.assertEqual(self.getOutput().count("We like Python's turtles!"), 100, 'Checking number of times message is printed')
      
   myTests().main()