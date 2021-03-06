.. activecode:: fourteenfive
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: accessor_functions
   :topics: Chapter14/accessor_functions
   :from_source: T
   :language: cpp

   Write your implementation of ``calculatePolar`` in the commented area of the active
   code below. Once you're done with that, write the ``getMag`` and ``getTheta``
   accessor functions. Read the comments in ``main`` to see how we'll test if your
   functions works. If you get stuck, you can reveal the extra problem at the end for help.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   class Complex
   {
     double real, imag;
     double mag, theta;
     bool cartesian, polar;

   public:
     Complex ();
     Complex (double r, double i);
     void calculateCartesian ();
     double getReal ();
     double getImag ();
     void calculatePolar ();
     double getMag ();
     double getTheta ();
   };

   void Complex::calculatePolar () {
     // ``calculatePolar`` should convert the real and imaginary parts
     // into magnitude and theta. Use the formula in the previous section.
     // Write your implementation here.
   }

   double Complex::getMag () {
     // ``getMag`` should return the magnitude.
     // Delete the return 0 and write your implementation here.
     return 0;
   }

   double Complex::getTheta () {
     // ``getMag`` should return the theta.
     // Delete the return 0 and write your implementation here.
     return 0;
   }

   int main() {
     Complex c1 (0.0, 1.0);
     // Magnitude should be 1, theta should be pi/2, or about 1.5708
     cout << c1.getMag() << ", " << c1.getTheta() << endl;
   }
   ====
   Complex::Complex () { cartesian = false;  polar = false; }

   Complex::Complex (double r, double i) {
     real = r;  imag = i;
     cartesian = true;  polar = false;
   }

   void Complex::calculateCartesian () {
     real = mag * cos (theta);
     imag = mag * sin (theta);
     cartesian = true;
   }

   double Complex::getReal () {
     if (cartesian == false) calculateCartesian ();
     return real;
   }

   double Complex::getImag () {
     if (cartesian == false) calculateCartesian ();
     return imag;
   }