.. actex:: TL_365_function_x**3
   :author: Tyler Luchko
   :difficulty: 1.0573103224
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.6666666667
   :total_students_attempting: 51
   :num_students_correct: 37.0
   :mean_clicks_to_correct: 1.972972973

   Write a function call ``pow3`` that takes a parameter ``x`` and returns ``float`` according to
   
   .. math::
      f(x) = x^3
   
   Using your function, print out values for :math:`x=-1.5, 0, 2.1`.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           def _pow3(x):
        return x**3
   
    for x in [-8.95, -0.05, 4.76, 9.83, -5.91]:
               self.assertAlmostEqual(pow3(x), _pow3(x), 7,
            "Checking pow3() for x={}".format(x))
   myTests().main()