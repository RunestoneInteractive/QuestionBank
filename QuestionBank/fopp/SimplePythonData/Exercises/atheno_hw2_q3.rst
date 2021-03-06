.. actex:: atheno_hw2_q3
   :author: Atheno Chen
   :difficulty: 1.1374386435
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 3.3333333333

   Write a program to accept the length of triangle sides ``a``, ``b``, and ``c`` as inputs and output the area of the triangle. Feel free to refer this video: https://www.khanacademy.org/math/geometry-home/geometry-volume-surface-area/heron-formula-tutorial/v/heron-s-formula It's good if you can also understand the proof.
   ~~~~
   # Python math module link: https://docs.python.org/3.7/library/math.html
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def test_radius(self):
           self.assertIn("a", self.getEditorText(), 'a variable')
           self.assertIn("b", self.getEditorText(), 'b variable')
           self.assertIn("c", self.getEditorText(), 'c variable')
           self.assertIn(str(math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/4)[:4], self.getOutput(), 'Checking answer.')
   myTests().main()