.. activecode:: KDL_ch13_4
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Tuples
   :subchapter: Exercises
   :topics: Tuples/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0888888889
   :total_students_attempting: 45
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 4.3571428571

   Using the code we created for parametric plotting. Create a function ``spiral(rmax,tlist)`` that makes a spiral that starts at rmax and spirals to r=0. This should auto scale based on the number of t values.
   
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           xvs,yvs=spiral(5,[0,15])
           self.assertIn('def spiral', self.getEditorText(), 'contains spiral function')
           self.assertEqual((min(xvs)**2+min(yvs)**2)**0.5, 0, "Testing the min radius is 0 for spiral(5,[0,15]).")
           self.assertEqual((max(xvs)**2+max(yvs)**2)**0.5, 5, "Testing the max radius is 5 for spiral(5,[0,15]).")
   
   
   
           
   myTests().main()