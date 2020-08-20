.. activecode:: KDL_exam2_1
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0188679245
   :total_students_attempting: 53
   :num_students_correct: 10.0
   :mean_clicks_to_correct: 10.1

   Create a text file called ``data_set.txt`` and load the supplied x and y data sets so that the file matches the style below. 
   
   ::
   
     x,y
     1,2
     2,4
     3,6
     4,8
     5,10
   
   ~~~~
   x=[1,2,3,4,5]
   y=[2,4,6,8,10]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue('open' in self.getEditorText(), 'A File created')
           self.assertTrue( '.write' in self.getEditorText(), 'Something written to file')
           self.assertTrue( open('data_set.txt','r').read()=='x,y\n1,2\n2,4\n3,6\n4,8\n5,10', 'File correct')
   
   myTests().main()