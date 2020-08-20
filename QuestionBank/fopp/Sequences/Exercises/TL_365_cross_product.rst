.. actex:: TL_365_cross_product
   :author: Tyler Luchko
   :difficulty: 1.1299314907
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1153846154
   :total_students_attempting: 78
   :num_students_correct: 34.0
   :mean_clicks_to_correct: 3.2058823529

   The cross product of two 3-vectors, :math:`\vec{a}=(a_1, a_2, a_3)` and :math:`\vec{b}=(b_1, b_2, b_3)`, is calculated as
   
   .. math::
      \vec{a}\times\vec{b} = (a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 -a_2b_1).
   
   For example, the norm of the vector
   :math:`\vec{a}=\left(3,0,-4\right)` and :math:`\vec{b}=\left(1,2,3\right)` is
   
   .. math::
      \vec{a}\times\vec{b} = (8, -13, 6).
   
   Ask the user for six values and store them as ``list`` s with type
   ``float`` and variable names ``vec_a`` and ``vec_b``.  Then print out
   :math:`\vec{a}\times\vec{b}`  as a ``list``.
   
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self): 
           ref_vec_c = [vec_a[1]* vec_b[2] - vec_a[2]*vec_b[1],
                 vec_a[2]* vec_b[0] - vec_a[0]*vec_b[2],
   vec_a[0]* vec_b[1] - vec_a[1]*vec_b[0]]
    output = self.getOutput().rstrip()
    self.assertEqual(output, str(ref_vec_c), 'Checking output')
    ref_escaped = '\['+str(ref_vec_c)[1:-1]+'\]'
    self.assertFalse(re.search(ref_escaped, self.getEditorText()), 'Checking hardcoding')
   myTests().main()