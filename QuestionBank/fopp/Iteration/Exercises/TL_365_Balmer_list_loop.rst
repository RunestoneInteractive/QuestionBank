.. actex:: TL_365_Balmer_list_loop
   :author: Tyler Luchko
   :difficulty: 1.2738159847
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1134020619
   :total_students_attempting: 97
   :num_students_correct: 37.0
   :mean_clicks_to_correct: 5.6486486486

   The wavelengths of the spectral lines from hydrogen are given by the Balmer series
   
   .. math::
      \frac{1}{\lambda} = R_\text{H}\left(\frac{1}{2^2} - \frac{1}{n^2}\right)\quad n=3,4,5,\dots
   
   where :math:`\lambda` is the wavelength in m and
   :math:`R_\text{H}=1.0974\times10^7~\text{m$^{-1}$}`.  Using a for-loop, compute the
   wavelengths of the first five spectral lines and store them in a
   list called ``wavelengths``.
   
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self): 
           _ryd = 1.094e7
    ref_wavelengths = lambda n : 1/(_ryd*(1/4 - 1/n**2))
    for i, n in enumerate(range(3, 8)):
        self.assertAlmostEqual(wavelengths[i], ref_wavelengths(n), 7, 'Checking n = '+str(n))
    self.assertFalse(re.search(r'(6.5609|4.8599|4.3392|4.1006|3.9689)', self.getEditorText()), 'Checking for hardcoding')
   
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)==0, 'Checking for-statements')
   myTests().main()