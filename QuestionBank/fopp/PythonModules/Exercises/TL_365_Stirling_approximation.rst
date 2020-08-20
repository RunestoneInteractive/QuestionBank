.. actex:: TL_365_Stirling_approximation
   :author: Tyler Luchko
   :difficulty: 1.5081420208
   :basecourse: fopp
   :chapter: PythonModules
   :subchapter: Exercises
   :topics: PythonModules/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0041666667
   :total_students_attempting: 240
   :num_students_correct: 67.0
   :mean_clicks_to_correct: 9.6268656716

   In statistical physics, it is common to use Stirling's approximation for :math:`N!`,
   
   .. math::
      N!\approx N^N e^{-N} \sqrt{2\pi N}.
   
   Obtain an integer from the user, assign it to ``N``, and print out, in order,
   :math:`N!`, Stirling's approximation, and the relative percent
   error. The relative percent error is calculated as
   
   .. math::
      \text{error} =  \left| \frac{\text{approx} - \text{exact}}{\text{exact}} \right| 100\%.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           ref_N_fact = math.factorial(N)
    ref_stirling = N**N * math.exp(-N) * math.sqrt(2 * math.pi * N)
    ref_rel_err = abs( (ref_stirling - ref_N_fact)/ref_N_fact) * 100
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
           self.assertAlmostEqual(float(output[0]), ref_N_fact, 7, 'Checking N!')
           self.assertAlmostEqual(float(output[1]), ref_stirling, 5, 'Checking Stirling Approximation')
           self.assertAlmostEqual(float(output[2]), ref_rel_err, 7, 'Checking the relative error')
    self.assertFalse(re.search(r'( *import *math *as| *from *math)', '\n'.join(editor)), 'Checking import statement')
   myTests().main()