.. activecode:: fourteenseven
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: a_function_on_complex_numbers
   :topics: Chapter14/a_function_on_complex_numbers
   :from_source: T
   :language: cpp

   The active code below uses the ``add`` function for ``Complex`` objects.
   As an exercise, write the ``subtract`` function for ``Complex`` objects
   in the commented area of the active code. If you get stuck, you can reveal
   the extra problem at the end for help. Once you are finished, feel
   free to modify the code and experiment around!
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
     void printCartesian ();
     void printPolar ();
   };

   Complex add (Complex& a, Complex& b);
   Complex subtract (Complex& a, Complex& b) {
     // ``subtract`` should subtract b from a and return
     // the difference of the two ``Complex`` objects.
     // Delete the existing code and write your implementation here.
     Complex c (0,0); return c;
   }

   int main() {
     Complex c1 (2.0, 3.0);
     Complex c2 (3.0, 4.0);
     Complex sum = add (c1, c2);
     sum.printCartesian();

     // Difference should be 1 + 1i
     Complex diff = subtract(c2, c1);
     diff.printCartesian();
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

   void Complex::calculatePolar () {
     mag = sqrt(pow(real, 2) + pow(imag, 2));
     theta = atan(imag / real);
     polar = true;
   }

   double Complex::getMag () {
     if (polar == false) {
       calculatePolar ();
     }
     return mag;
   }

   double Complex::getTheta () {
     if (polar == false) {
       calculatePolar ();
     }
     return theta;
   }

   void Complex::printCartesian () {
     cout << getReal() << " + " << getImag() << "i" << endl;
   }

   void Complex::printPolar () {
     cout << getMag() << " e^ " << getTheta() << "i" << endl;
   }

   Complex add (Complex& a, Complex& b) {
     double real = a.getReal() + b.getReal();
     double imag = a.getImag() + b.getImag();
     Complex sum (real, imag);
     return sum;
   }