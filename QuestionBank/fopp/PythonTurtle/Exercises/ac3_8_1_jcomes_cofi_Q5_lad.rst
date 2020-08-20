.. actex:: ac3_8_1_jcomes_cofi_Q5_lad
   :author: Lynda Danielson
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Write a program that prints ``Python programming is fun!`` 99 times.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn("Python programming is fun!", self.getEditorText(), 'Checking the message appears in the code.\nNote: Capitalization, punctuation, and spacing matter!')
           self.assertEqual(self.getOutput().count("Python programming is fun!"), 99, 'Checking number of times message is printed')
      
   myTests().main()