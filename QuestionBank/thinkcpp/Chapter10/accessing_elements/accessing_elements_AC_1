.. activecode:: accessing_elements_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: accessing_elements
   :topics: Chapter10/accessing_elements
   :from_source: T
   :language: cpp

   Take a look at the active code below. We can modify the vectors by accessing
   its elements.
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   void print_vec(vector<int> vec) {
       cout << "[";
       for (size_t i = 0; i < vec.size() - 1; ++i) {
           cout <<  vec[i] << ",";
       }
       cout << vec[vec.size()-1];
       cout << "]" << endl;
   }

   int main() {
       vector<int> count = {1,2,3,4};
       cout << "Before we make any changes, count = "; print_vec(count);
       count[0] = 7;
       count[1] = count[0] * 2;
       count[2]++;
       count[3] -= 60;
       cout << "After we made the above changes, count = "; print_vec(count);
   }