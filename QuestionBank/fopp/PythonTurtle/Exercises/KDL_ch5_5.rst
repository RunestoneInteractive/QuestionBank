.. activecode:: KDL_ch5_5
   :author: Kaelyn Leake
   :difficulty: 1.1472556894
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0158730159
   :total_students_attempting: 63
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 3.5

   Use the turtle module to create a turtle ``tuck``. Use tuck to draw a box with it's center at (:math:`x=0`, :math:`y=0`). The width of the box should be `100` and the height of the box should be `200`.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertTrue('import turtle' in self.getEditorText(), 'Contains Turtle module')
           self.assertTrue('tuck' in self.getEditorText(), 'Contains tuck')
           self.assertTrue((tuck.xcor()**2)**.5*2==100, 'x makes sense')
           self.assertTrue((tuck.ycor()**2)**.5*2==200, 'y makes sense')
   
   
           
   myTests().main()