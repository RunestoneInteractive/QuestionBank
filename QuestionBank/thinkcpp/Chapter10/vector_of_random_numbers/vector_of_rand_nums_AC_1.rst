.. activecode:: vector_of_rand_nums_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: vector_of_random_numbers
   :topics: Chapter10/vector_of_random_numbers
   :from_source: T
   :language: cpp

   Try running the active code below!
   ~~~~
   #include <iostream>
   #include <vector>
   using namespace std;

   vector<int> randomVector (int n, int upperBound);
   void printVector (const vector<int>& vec);

   int main() {
       int numValues = 20;
       int upperBound = 10;
       vector<int> vector = randomVector (numValues, upperBound);
       printVector (vector);
   }

   ====

   vector<int> randomVector (int n, int upperBound) {
      vector<int> vec (n);
      for (size_t i = 0; i<vec.size(); i++) {
         vec[i] = random () % upperBound;
      }
      return vec;
   }

   void printVector (const vector<int>& vec) {
      for (size_t i = 0; i<vec.size(); i++) {
         cout << vec[i] << " ";
      }
   }