.. activecode:: order_of_operations_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: OrderofOperations
   :topics: Chapter2/OrderofOperations
   :from_source: T
   :language: cpp
   :caption: The Role of Parentheses

   Observe the output of the code below to see how the placement of parentheses
   can change the result of a calculation.

   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       cout << (2 * 3) - 1 << endl;
       cout << 2 * (3 - 1) << endl;
       cout << 2 / 3 - 1 << endl;
       cout << 2 / (3 -1) << endl;
   }