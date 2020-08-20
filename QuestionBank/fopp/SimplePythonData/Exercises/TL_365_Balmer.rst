.. actex:: TL_365_Balmer
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1052631579
   :total_students_attempting: 57
   :num_students_correct: 31.0
   :mean_clicks_to_correct: 4.4193548387

   The wavelengths of the spectral lines from hydrogen are given by the Balmer series
   
   .. math::
      \frac{1}{\lambda} = R_\text{H}\left(\frac{1}{2^2} - \frac{1}{n^2}\right)\quad n=3,4,5,\dots
   
   where :math:`\lambda` is the wavelength in m and  :math:`R_\text{H}=1.0974\times10^7~\text{m$^{-1}$}`.
   Print out the wavelengths of the first five spectral lines.
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(re.search(str(6.5609)[:6], self.getOutput()), 'Checking answer.')
    self.assertTrue(re.search(str(4.8599)[:6], self.getOutput()), 'Checking answer.')
    self.assertTrue(re.search(str(4.3392)[:6], self.getOutput()), 'Checking answer.')
    self.assertTrue(re.search(str(4.1006)[:6], self.getOutput()), 'Checking answer.')
    self.assertTrue(re.search(str(3.9689)[:6], self.getOutput()), 'Checking answer.')  
   myTests().main()