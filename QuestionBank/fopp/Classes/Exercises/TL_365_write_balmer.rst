.. actex:: TL_365_write_balmer
   :author: Tyler Luchko
   :difficulty: 1.4609743321
   :basecourse: fopp
   :chapter: Classes
   :subchapter: Exercises
   :topics: Classes/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0975609756
   :total_students_attempting: 41
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 8.8260869565

   The wavelengths of the spectral lines from hydrogen are given by the Balmer series
   
   .. math::
      \frac{1}{\lambda} = R_\text{H}\left(\frac{1}{2^2} - \frac{1}{n^2}\right)\quad n=3,4,5,\dots
   
   where :math:`\lambda` is the wavelength in m and
   :math:`R_\text{H}=1.0974\times10^7~\text{m$^{-1}$}`.
   
   Compute the first 10 wavelengths from the Balmer series and write
   them to a file call ``balmer.dat`` with one :math:`n` value and its wavelength per line
   in CSV format.
   
   Hint: if you already have a solution for a previous the Balmer
   series question, copy and paste here to reuse the code.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self): 
           _ryd = 1.094e7
    ref_wavelengths = lambda n : 1/(_ryd*(1/4 - 1/n**2))
    with open('balmer.dat', 'r') as fh:
        for _n in range(3, 13):
            n, wavelength = fh.readline().split(',')
              self.assertEqual(int(n), _n, 'Checking n = '+str(n))
              self.assertAlmostEqual(float(wavelength), ref_wavelengths(_n), 7, 'Checking wavelength for n = '+str(n))
    self.assertFalse(re.search(r'(6.5609|4.8599|4.3392|4.1006|3.9689)', self.getEditorText()), 'Checking for hardcoding')
   
   myTests().main()