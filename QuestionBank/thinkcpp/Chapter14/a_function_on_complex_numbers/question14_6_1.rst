.. parsonsprob:: question14_6_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: a_function_on_complex_numbers
   :topics: Chapter14/a_function_on_complex_numbers
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the ``subtract`` function,
   which should return the difference of two ``Complex`` objects.
   -----
   Complex subtract (Complex& a, Complex& b) {
   =====
   Complex subtract (Complex& a) {                         #paired
   =====
      double real = a.getReal() - b.getReal();
   =====
      double real = a.getReal() + b.getReal();                         #paired
   =====
      double imag = a.getImag() - b.getImag();
   =====
      Complex diff (real, imag);
   =====
      Complex diff (imag, real);                         #paired
   =====
      return diff;
   }
   =====
      return sum;                         #paired
   }