.. parsonsprob:: question14_3_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: complex_numbers
   :topics: Chapter14/complex_numbers
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write a constructor that uses parameters to
   initialize the magnitude and theta, but does not calculate
   the real and imaginary parts. Set the cartesian flag to false.
   -----
   Complex (double m, double t)
   =====
   Complex (int m, int t)                         #paired
   =====
   {
   =====
     mag = m;   theta = t;
   =====
     cartesian = false;   polar = true;
   =====
     cartesian = true;   polar = false;                         #paired
   =====
   }