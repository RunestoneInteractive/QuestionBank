.. activecode:: fourteenfour
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: accessor_functions
   :topics: Chapter14/accessor_functions
   :from_source: T
   :language: cpp

   Take a look at the active code below, which uses the ``getReal``
   accessor function.
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
     Complex () { cartesian = false;  polar = false; }
     Complex (double r, double i)
     {
       real = r;  imag = i;
       cartesian = true;  polar = false;
     }
     void calculateCartesian ()
     {
       real = mag * cos (theta);
       imag = mag * sin (theta);
       cartesian = true;
     }
     double getReal ()
     {
       if (cartesian == false) calculateCartesian ();
       return real;
     }
     double getImag ()
     {
       if (cartesian == false) calculateCartesian ();
       return imag;
     }
   };

   int main() {
     Complex c1 (5.0, 3.5);
     cout << c1.getReal() << ", " << c1.getImag() << endl;
   }