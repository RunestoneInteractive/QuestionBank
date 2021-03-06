.. activecode:: fourteenthree
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: complex_numbers
   :topics: Chapter14/complex_numbers
   :from_source: T
   :language: cpp

   Now take a look at this second piece of active code. What if we decide we want
   to represent a ``Triangle`` in a different way? Because the way we represent a
   ``Triangle`` is private, we can easily change the implementation while keeping
   the interface the same. Now, ``Triangle`` is represented by two sides and the
   angle between them. Notice how our ``main`` function is the exact same as before.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   class Triangle {
     private:
       double side_a, side_b, angle;
     public:
       Triangle () {side_a = 1; side_b = 1; angle = 60;}
       Triangle (double a_in, double b_in, double c_in) {
         side_a = a_in;
         side_b = b_in;
         // Law of Cosines: c^2 = a^2 + b^2 - 2abcosC
         angle = acos((pow(a_in, 2) + pow(b_in, 2) - pow(c_in, 2))
                      / 2 * a_in * b_in);
       }
       double perimeter () {
         return side_a + side_b +
                sqrt(pow(side_a, 2) + pow(side_b, 2)
                - 2 * side_a * side_b * cos(angle));
       }
   };

   int main() {
     Triangle t1(3, 4, 5);
     cout << t1.perimeter();
   }