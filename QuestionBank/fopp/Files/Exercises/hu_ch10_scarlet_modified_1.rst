.. activecode:: hu_ch10_scarlet_modified_1
   :author: Sean Joyce
   :difficulty: 1.3681392236
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1428571429
   :total_students_attempting: 14
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 7.25

   I have given you access to a text file named ``scarlet.txt``, 
   which is a file containing the entire text of Sir Arthur
   Conan Doyle's *A Study in Scarlet*, a Sherlock Holmes
   mystery.
   
   Your task is to find out how often the words *red* and
   *scarlet* appear in the story.  (Do not worry about 
   uppercase or mixed-case: assume the words in which you 
   are interested appear in all lowercase.)
   
   Assign to variable ``red_count`` the number of times the
   word "red" (no quotes) appears in the file; assign to
   variable ``scarlet_count`` the number of times the word
   "scarlet" (no quotes) appears in the file.
   
   Your program should not have any output, *i.e.* there 
   should be no ``print`` statements in your code. It should
   merely assign the values to the two variables as indicated. 
   I have started the code for you.
   ~~~~
   # file name is 'scarlet.txt'
   fname = 'scarlet.txt'
   filevar = open(fname, 'r')
   
   
   # your code here
   
   
   # do not delete the line below
   filevar.close()
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn("open(", self.getEditorText(), 'Contains open for file')
           self.assertEqual(red_count, 367, "Checking value of red_count")
           self.assertEqual(scarlet_count, 2, "Checking value of scarlet_count")
   
           
   myTests().main()