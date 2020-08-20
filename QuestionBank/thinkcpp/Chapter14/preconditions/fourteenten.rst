.. activecode:: fourteenten
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: preconditions
   :topics: Chapter14/preconditions
   :from_source: T
   :language: cpp

   The active code below uses the updated ``calculateCartesian`` with assert statements.
   Notice how because ``c1`` is not in polar, the assert statement in ``calculateCartesian``
   fails and thus we get an error.
   ~~~~
   #include <iostream>
   #include <cmath>
   #include <cassert>
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
     void setPolar (double m, double t);
     void setCartesian (double r, double i);
   };

   Complex add (Complex& a, Complex& b);
   Complex subtract (Complex& a, Complex& b);
   Complex mult (Complex& a, Complex& b);

   int main() {
     Complex c1 (5.4, 3.2);
     // This will output an error statement stating that
     // "Assertion 'polar' failed."
     c1.calculateCartesian();
   }
   ====
   Complex::Complex () { cartesian = false;  polar = false; }

   Complex::Complex (double r, double i) {
     real = r;  imag = i;
     cartesian = true;  polar = false;
   }

   void Complex::calculateCartesian () {
     assert (polar);
     real = mag * cos (theta);
     imag = mag * sin (theta);
     cartesian = true;
     assert (polar && cartesian);
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

   Complex subtract (Complex& a, Complex& b) {
     double real = a.getReal() - b.getReal();
     double imag = a.getImag() - b.getImag();
     Complex diff (real, imag);
     return diff;
   }

   void Complex::setPolar (double m, double t) {
     mag = m;  theta = t;
     cartesian = false;  polar = true;
   }

   Complex mult (Complex& a, Complex& b) {
     double mag = a.getMag() * b.getMag();
     double theta = a.getTheta() + b.getTheta();
     Complex product;
     product.setPolar (mag, theta);
     return product;
   }

   void Complex::setCartesian (double r, double i) {
     real = r;    imag = i;
     cartesian = true;  polar = false;
   }