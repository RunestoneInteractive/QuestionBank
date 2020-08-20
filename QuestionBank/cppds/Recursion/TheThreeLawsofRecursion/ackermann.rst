.. activecode:: ackermann
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: TheThreeLawsofRecursion
   :topics: Recursion/TheThreeLawsofRecursion
   :from_source: T
   :language: cpp
   :nocodelens:

   //ackermann function example
   #include <iostream>
   using namespace std;

   unsigned int ackermann(unsigned int m, unsigned int n) {
      if (m == 0) {//Base case
         return n + 1;
      }
      if (n == 0) {
         return ackermann(m - 1, 1);// subtract, move to base case
      }
      //notice a call to the ackermann function as a parameter
      //for another call to the ackermann function. This is where
      //it gets unrealistically complicated.
      return ackermann(m - 1, ackermann(m, n - 1));//subtract here too
   }

   int main(){
      //compute the ackermann function.
      //Try replacing the 1,2 parameters with 4,3 and see what happens
      cout << ackermann(1,2) << endl;
      return 0;
   }