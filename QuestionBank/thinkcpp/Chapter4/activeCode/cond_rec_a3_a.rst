.. activecode:: cond_rec_a3_a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Below is one way to fix the program.  The infinite recursion
   happens when we use an odd number as an argument.  By checking
   that a number is less than 99, the highest numbers to recurse
   are 98 and 97.  ``98 + 2 == 100`` and ``97 + 2 == 99``, so we
   never count past 100.
   ~~~~
   #include <iostream>
   using namespace std;

   void countBy2 (int num) {
       if (num < 9) {
           cout << num;
           countBy2 (num + 2);
       }
       else {
           cout << num << endl;
           cout << "Done counting!";
       }
   }

   int main () {
       countBy2(6);
   }