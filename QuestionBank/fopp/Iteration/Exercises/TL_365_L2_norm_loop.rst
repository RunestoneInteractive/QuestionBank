.. actex:: TL_365_L2_norm_loop
   :author: Tyler Luchko
   :difficulty: 1.2666964153
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.035971223
   :total_students_attempting: 139
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 5.5277777778

   The :math:`L^{2}\text{-norm}` is the most common method for calculating
   the norm or magnitude of a vector. For an :math:`N\text{-dimensional}` vector, the
   :math:`L^{2}\text{-norm}` is calculated as
   
   .. math::
      \left|\vec{v}\right|=\sqrt{ \sum_{i=1}^N v_i^{2}}.
   
   For example, the norm of the vector
   :math:`\vec{v}=\left(3,0,-4\right)` is
   
   .. math::
      \left|\vec{v}\right|=\sqrt{\left(3\right)^{2}+\left(0\right)^{2}+\left(-4\right)^{2}}=5.
   
   Compute and print out the :math:`L^{2}\text{-norm}` of the vectors defined below.
   
   ~~~~
   vec_1 = [3,0,-4]
   vec_2 = [17.4, 32.3, -3.14, 79, -55]
   vec_3 = [-39.33, 81.27, -80.88, 85.08, -35.9, 86.42, 49.23, -31.41, 47.38, -80.54]
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    
           norm = lambda vec: math.sqrt(sum([v**2 for v in vec]))
    for vec, line in zip([vec_1, vec_2, vec_3], output):
        self.assertAlmostEqual(float(line), norm(vec), 7, 'Checking output for '+str(vec))
        
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)>=1 and len(inner_loops)>=0, 'Checking for-statements')
   myTests().main()