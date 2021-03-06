.. actex:: TL_365_function_euler_1d
   :author: Tyler Luchko
   :difficulty: 1.2489959839
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1212121212
   :total_students_attempting: 33
   :num_students_correct: 22.0
   :mean_clicks_to_correct: 5.2272727273

   Consider the expression for radioactive decay
   
   .. math::
      
      \frac{dN}{dt} = -\lambda N
      
   where :math:`N` is the number of particles, :math:`t` is time and
   :math:`\lambda` is a decay constant. If we have a value for the
   number of particles at the current time, :math:`N(t)`, we can
   calculate the number of particles at :math:`\Delta t` in the future
   from
   
   .. math::
      
      N(t+\Delta t) = N(t) + \frac{dN}{dt}\Delta t = N(t) -\lambda N(t) \Delta t
        
   Write a function call ``decay`` that takes a list of the number of
   particles a previous times, the decay constant, ``decay_const``, the
   time step ``delta_t``, and the number of time steps, ``nsteps``.
   It should update the input list by using the last value in the list
   as the current number of particles and appending a new value for
   each time step.
   
   E.g., the function call
   
   .. code:: python
      
      decay( [10], 2, .01, 5)
      
   we expect the output
   
   .. code::
   
      [10, 9.8, 9.604, 9.41192, 9.2236816, 9.039207968]
   
   For 
   
   .. code:: python
   
      decay( [100, 200, 300], 2, .01, 5)
   
   we expect the output 
   
   .. code::
      
      [100, 200, 300, 294.0, 288.12, 282.3576, 276.710448, 271.17623904]
      
   since ``100`` and ``200`` are not used.  
   
   Note: the approach we are using here is called the Euler method.
   There are much better methods for integrating ordinary differential
   equation initial values problems but they all use the same basic
   approach of iteratively updating from an initial value.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import math
   class myTests(TestCaseGui):
       def testOne(self):
             _decay = lambda particles, decay_const, dt, nsteps: [particles.append(particles[-1] - decay_const*particles[-1]*dt) for i in range(nsteps)][0]
   
             def test_decay(particles, decay_const, delta_t, nsteps):
                 _particles = particles[:]
                 particles_ref = particles[:]
                 self.assertEqual(decay(particles, decay_const, delta_t, nsteps),
                     _decay(_particles, decay_const, delta_t, nsteps), 'Checking output')
                 self.assertEqual(particles[:-nsteps], particles_ref,
                     'Checking that the original elements haven\'t changed for {}, {}, {}, {}'.format(particles_ref, decay_const, delta_t, nsteps))
                 self.assertEqual(len(particles), len(_particles), "Checking list length")
                 for i in range(len(particles)):
                     self.assertAlmostEqual(particles[i], _particles[i], 7, 'Checking elements of the updated list')
   
             test_decay([10], 2, .01, 5)
             test_decay([100, 200, 300], 2, .01, 5)
             test_decay([1000], 0.5, .001, 20)
   
   myTests().main()