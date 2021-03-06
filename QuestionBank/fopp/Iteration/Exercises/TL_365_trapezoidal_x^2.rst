.. actex:: TL_365_trapezoidal_x^2
   :author: Tyler Luchko
   :difficulty: 1.8688085676
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 61
   :num_students_correct: 16.0
   :mean_clicks_to_correct: 15.75

   One of the easiest methods for numerically integrating functions is
   the `trapezoidal method
   <https://en.wikipedia.org/wiki/Trapezoidal_rule>`_. To compute the
   integral, we evaluate the function at regular intervals,
   :math:`\Delta x`, starting from the lower bound and concluding with
   the upper bound and combining the result as
   
   .. math::
      \int_a^b f(x) \approx \Delta x \left( \frac{f(a) + f(b)}{2} + \sum_{k=1}^{N-1} f(x_k)\right)
   
   When computing integrals like this, it is best to determine
   :math:`\Delta x` from the number of evaluation point rather than
   the other way around. I.e., if you wish to evaluate the integral from ``a`` to ``b`` using ``N=10``, then 
   
   .. code:: python
   
      N = 10
      dx = (b-a)/(N-1)
      
   This prevents problems with round-off error when your interval is not precisely divisible by your :math:`\Delta x`.
   
   Use the trapezoidal method to evaluate the integral 
   
   .. math::
      \int_0^2 x^2\, dx
   
   with ``N=11`` and print the result.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           sum = 0
    N=11
    dx = (2-0)/(N-1)
    for i in range(1,10):
        sum += (i*dx)**2
    sum += (0 + 2**2)/2
    integral = sum*dx
    # check the answer
    self.assertAlmostEqual(float(self.getOutput()), integral, 7, 'Checking answer')
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
   
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)>=0, 'Checking for-statements')
   myTests().main()