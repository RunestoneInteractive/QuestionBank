.. actex:: TL_365_class_charged_particle
   :author: Tyler Luchko
   :difficulty: 1.3790233397
   :basecourse: fopp
   :chapter: Classes
   :subchapter: Exercises
   :topics: Classes/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1458333333
   :total_students_attempting: 48
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 7.4347826087

   Create a class called ``Charge`` that describes a charged particle,
   and define ``__init__()`` and ``potential_at()``
   methods. ``__init__`` should initialize the ``x``, ``y``, and ``z``
   positions of the particle and the charge, ``q``. ``potential_at()``
   should take a 3D position to calculate a potential at and return
   the value of the potential
   
   .. math::
      
      V=k_e\frac{q}{r}
      
   where :math:`k_e=8.99\times10^9\,\text{N}\cdot
   \text{m}^2/\text{C}^2`.  Test your class by creating a charged
   particle at :math:`(1,2,3)` and calculating its potential at
   :math:`(2,3,4)`.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import math
   class myTests(TestCaseGui):
       def testOne(self):
      class _Charge:
          def __init__(self, x, y, z, q):
       self.x = x
       self.y = y
       self.z = z
       self.q = q
   def potential_at(self, x, y, z):
       return 8.99e9*self.q/( (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2 )**0.5
       
      self.assertEqual(Charge(1,2,3,4).potential_at(2,3,4),
          _Charge(1,2,3,4).potential_at(2,3,4),
          'Checking potential(2,3,4) for Charge(1, 2, 3, 4)')
      self.assertEqual(Charge(-6.54,-8.99,8.03,6.27).potential_at(1.52,-6.61,3.92),
          _Charge(-6.54,-8.99,8.03,6.27).potential_at(1.52,-6.61,3.92),
          'Checking potential(2,3,4) for Charge(1, 2, 3, 4)')
   myTests().main()