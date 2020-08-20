.. activecode:: vector_size_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: vector_size
   :topics: Chapter10/vector_size
   :from_source: T
   :language: cpp

   Try running the active code below!
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   int main() {
       vector<int> count = {1,2,3,4};
       size_t i;
       for (i = 0; i < count.size(); i++) {
           cout << count[i] << endl;
       }
   }