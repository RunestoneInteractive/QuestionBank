.. activecode:: cond_rec_a3q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Fix the infinite recursion in the code below.  The function
   should not count any numbers after 10 (the highest numbers
   that should print are 9 or 10).  When it is done counting,
   the function should print that.
   ~~~~
   #include <iostream>
   using namespace std;

   void countBy2 (int num) {
       if (num != 10) {
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