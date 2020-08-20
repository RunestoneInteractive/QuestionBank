.. actex :: TL_365_wvu_forloop_oddnumbers
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2621359223
   :total_students_attempting: 103
   :num_students_correct: 66.0
   :mean_clicks_to_correct: 3.6212121212

   Write a for loop that prints the odd numbers from 1 to 101, with one value on each line.
   ~~~~
   # Your code goes here
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           output = self.getOutput().rstrip().split('\n')
    # check the answer
    self.assertEqual(len(output), 51)
    for i, line in enumerate(output):
        self.assertEqual(line.rstrip(), str(i*2+1), 'Checking line '+str(i))
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
   
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)>=0, 'Checking for-statements')
   myTests().main()