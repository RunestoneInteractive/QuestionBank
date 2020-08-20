.. actex:: TL_365_sequence_10
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.8333333333
   :total_students_attempting: 18
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 1.2352941176

   Output the sequence of numbers
   
   .. math::
      0,1,2,\dots,8,9,10
   
   with one value on each line.
      
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
        self.assertEqual(line.rstrip(), str(i), 'Checking line '+str(i))
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
   
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)>=0, 'Checking for-statements')
   myTests().main()