.. activecode:: TL_365_vrms
   :author: Tyler Luchko
   :difficulty: 1.0911318229
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2558139535
   :total_students_attempting: 86
   :num_students_correct: 53.0
   :mean_clicks_to_correct: 2.5471698113

   Write a program to print out the root mean squared speed of
   hydrogen molecules in a gas where
   
   .. math:: v_\text{rms} = \sqrt{\frac{3k_\text{B}T}{m_0}}
   
   where :math:`k_\text{B}=1.381\times 10^{-23}~\text{J/K}` is
   Boltzmann's constant, :math:`m_0=2(1.67\times10^{-27}~\text{kg})`
   and :math:`T` is the temperature supplied by the user. Please use
   the variable ``temperature`` to hold the user supplied temperature as
   a ``float``.
   
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
    kb = 1.381e-23
           m_0 = 2*1.67e-27
           self.assertTrue(re.search(str((3*kb*temperature/m_0)**(1/2))[:5], self.getOutput()), 'Checking answer.')
   myTests().main()