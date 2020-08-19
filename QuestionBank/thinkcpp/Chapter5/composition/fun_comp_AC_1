.. activecode:: fun_comp_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: composition
   :topics: Chapter5/composition
   :from_source: T
   :language: cpp
   :caption: Function Composition

   This program shows you how the distance and area functions are
   composed in the fred function to calculate the area of a circle
   if we only know the coordinates of the center, and one other point
   of the circle.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   double distance (double x1, double y1, double x2, double y2) {
       double dx = x2 - x1;
       double dy = y2 - y1;
       double dsquared = dx * dx + dy * dy;
       double result = sqrt (dsquared);
       return result;
   }

   double area (double radius) {
       double area = 3.14 * (radius * radius);
       return area;
   }

   double fred (double xc, double yc, double xp, double yp) {
       return area (distance (xc, yc, xp, yp));
   }

   int main () {
       double circle_area = fred (1.0, 2.0, 4.0, 6.0);
       cout << circle_area << endl;
       return 0;
   }