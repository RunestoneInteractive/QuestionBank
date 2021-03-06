.. actex:: TL_365_sequence_x^2
   :author: Tyler Luchko
   :difficulty: 1.1835559291
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1782178218
   :total_students_attempting: 101
   :num_students_correct: 43.0
   :mean_clicks_to_correct: 4.1162790698

   Evaluate and output
   
   .. math::
      f(x) = x^2
      
   for 
   
   .. math::
      x=0,0.2, 0.4, 0.8\dots,1.6,1.8,2.0
   
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           output = self.getOutput().rstrip().split('\n')
    self.assertEqual(len(output), 11)
    # check the answer
    for i, line in enumerate(output):
        self.assertAlmostEqual(float(line.rstrip()), (i*0.2)**2, 7, 'Checking line '+str(i))
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
   
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)>=0, 'Checking for-statements')
   myTests().main()