.. activecode:: for_loops_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: for_loops
   :topics: Chapter10/for_loops
   :from_source: T
   :language: cpp

   Run the active code below, which uses a ``while`` loop.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   int main() {
       vector<int> count = {1,2,3,4};
       int i = 0;
       while (i < 4) {
           cout << count[i] << endl;
           i++;
       }
   }