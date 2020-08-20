.. actex:: TL_365_rainfall_above_ave
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1238095238
   :total_students_attempting: 105
   :num_students_correct: 45.0
   :mean_clicks_to_correct: 6.5333333333

        
   The average monthly rainfall in inches recorded at the Van Nuys Airport for
   2018 is stored in the ``rainfall`` variable provided below.
   
   Create a new ``list`` called ``above_ave`` and add a ``True`` item
   for each month that was above average rainfall and a ``False`` item
   for each month below average. 
        
   ~~~~
   
   rainfall = [1.79, 0.18, 3.81, 0.03, 0.04, 0.00, 0.00, 0.00, 0.00, 0.32, 0.97, 2.60]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
    total = sum(rainfall)
    mean = total/len(rainfall)
    _above_ave = []
    for v in rainfall:
        _above_ave.append(v>mean)
   
    self.assertEqual(above_ave, _above_ave, 'Checking list')
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==2 and len(inner_loops)==0, 'Checking for-statements')
   myTests().main()