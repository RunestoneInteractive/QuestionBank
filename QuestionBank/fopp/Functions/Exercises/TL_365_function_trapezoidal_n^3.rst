.. actex:: TL_365_function_trapezoidal_n^3
   :author: Tyler Luchko
   :difficulty: 2.1878625614
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 36
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 21.1666666667

   Write a function to implement the `trapezoidal method
   <https://en.wikipedia.org/wiki/Trapezoidal_rule>`_, 
   
   .. math::
      \int_a^b f(x)\, dx \approx \Delta x \left( \frac{f(a) + f(b)}{2} + \sum_{k=1}^{N-1} f(x_k)\right),
   
   where :math:`a` and :math:`b` are the lower and upper bounds of the
   integral, :math:`f(x)` is the integrand, :math:`N` is the number of
   points that the integrand is evaluated at, and :math:`\Delta x` is
   the interval between evaluation points.
   
   Your function should be called ``int_trapz`` and should take as
   parameters the integrand, lower and upper bounds, and the number of
   evaluation points.  It should return the estimated value of the
   integral.
   
   Use your function to evaluate the integral
   
   .. math::
      \int_{-1}^3 x^3\, dx
      
   using 101 evaluation points and print out the result.
   
   Hint: use your and ``pow3`` functions from a previous problem.
   
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
       
           def _cubed(x):
        return(x**3)
           def _squared(x):
        return(x**2)
       
           def _int_trapz(func, a, b, N):
        sum = 0
        dx = (b-a)/(N-1)
        for i in range(1,N-1):
            sum += func(a + i*dx)
        sum += (func(a) + func(b))/2
        return sum*dx
   
           # check the answer
    self.assertAlmostEqual(int_trapz(_cubed, -1, 3, 101) , _int_trapz(_cubed, -1, 3, 101), 7, 'Integrating x^3 from -1 to 3 with 101 points')
    self.assertAlmostEqual(int_trapz(_cubed, 10, 20, 51) , _int_trapz(_cubed, 10, 20, 51), 7, 'Integrating x^3 from 10 to 20 with 51 points')
    self.assertAlmostEqual(int_trapz(_squared, -1, 3, 101) , _int_trapz(_squared, -1, 3, 101), 7, 'Integrating x^3 from -1 to 3 with 101 points')
    self.assertAlmostEqual(float(self.getOutput()), _int_trapz(_cubed, -1, 3, 101), 7, 'Checking output')
   myTests().main()