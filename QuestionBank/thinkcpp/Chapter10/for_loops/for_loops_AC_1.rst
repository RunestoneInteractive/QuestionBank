.. activecode:: for_loops_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: for_loops
   :topics: Chapter10/for_loops
   :from_source: T
   :language: cpp

   Run the active code below, which uses a ``for`` loop.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   int main() {
       vector<int> count = {1,2,3,4};
       int i;
       for (i = 0; i < 4; i++) {
           cout << count[i] << endl;
       }
   }