.. parsonsprob:: question14_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: accessor_functions
   :topics: Chapter14/accessor_functions
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the ``getMag`` function,
   which should return the magnitude of a ``Complex`` object.
   -----
   double Complex::getMag () {
   =====
   void Complex::getMag () {                         #paired
   =====
      if (polar == false) {
   =====
         calculatePolar ();
      }
   =====
      return mag;
   }