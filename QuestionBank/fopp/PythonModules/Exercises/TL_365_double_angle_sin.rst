.. actex:: TL_365_double_angle_sin
   :author: Tyler Luchko
   :difficulty: 1.151618821
   :basecourse: fopp
   :chapter: PythonModules
   :subchapter: Exercises
   :topics: PythonModules/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.192
   :total_students_attempting: 125
   :num_students_correct: 54.0
   :mean_clicks_to_correct: 3.5740740741

   Use the double angle formula,
   
   .. math::
      \sin(2\theta) = 2\sin(\theta)\cos(\theta),
   
   to compute and print 
   
   .. math::
      \sin(\pi/4)
   
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           output = self.getOutput()
    editor = self.getEditorText()
           self.assertAlmostEqual(float(output), 2*math.sin(math.pi/8)*math.cos(math.pi/8), 7, 'Checking output')
    self.assertFalse(re.search(r'(0.70710|math.sin *\( *math.pi */ *4 *\))', editor), 'Checking for hardcoding')
    self.assertFalse(re.search(r'( *import *math *as| *from *math)', editor), 'Checking import statement')
   myTests().main()