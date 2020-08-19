.. actex:: TL_365_function_lorentzian
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1666666667
   :total_students_attempting: 36
   :num_students_correct: 22.0
   :mean_clicks_to_correct: 2.7272727273

   The `Lorentzian function
   <https://en.wikipedia.org/wiki/Spectral_line_shape#Lorentzian>`_
   is often used to fit frequency spectra.  It is given by
   
   .. math::
      L\left(p\right)=\frac{1}{1+\left(\frac{p^{0}-p}{w/2}\right)^{2}}
   
   where :math:`p` is the frequency, :math:`p^0` is the frequency of
   maximum intensity, and :math:`w` is the full width at half maximum.
   
   Write a function called ``lorzentian`` that takes parameters
   ``freq`` (:math:`p`), ``freq_max`` (:math:`p^0`), and ``width``
   (:math:`w`) and returns the value of the Lorentzian function as a ``float``.
   
   
   Print the results of your function for 
   
   .. code:: python
   
      freq=0.5,  freq_max=0,   width=1
      freq=-0.5, freq_max=0,   width=1
      freq=0.5,  freq_max=0.5, width=1
      freq=0.5,  freq_max=0,   width=2
      freq=-0.5, freq_max=0.5, width=2
   
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
   
    def _lorzentian(freq, freq_max, width):
        inv_lorzentian = 1+ ( (freq - freq_max)/(width/2) )**2
        return 1/inv_lorzentian
        
    freqs = [0.5, -0.5, 0.5, 0.5, -0.5, 1]
    freq_maxs = [0, 0, 0.5, 0, 0.5, 2]
    widths = [1, 1, 1, 2, 2, 2]
   
    output_lines = self.getOutput().split()
    
    for freq, freq_max, width in zip(freqs, freq_maxs, widths):
        self.assertAlmostEqual(lorzentian(freq, freq_max, width),
            _lorzentian(freq, freq_max, width), 7,
            "Checking lorzentian({}, {}, {})".format(freq, freq_max, width))
           for i in range(len(freqs)-1):
        self.assertAlmostEqual(float(output_lines[i]),
            _lorzentian(freqs[i], freq_maxs[i], widths[i]), 7,
            "Checking output for lorzentian({}, {}, {})".format(freqs[i], freq_maxs[i], widths[i]))
   
    self.assertAlmostEqual(lorzentian(freq=1, freq_max=1, width=1),
        _lorzentian(1, 1, 1), 7,
        "Checking parameter names")
   
   myTests().main()