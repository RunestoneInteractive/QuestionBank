.. activecode:: lst_recstackcpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: StackFramesImplementingRecursion
   :topics: Recursion/StackFramesImplementingRecursion
   :from_source: T
   :caption: Converting an Integer to a String  Using a Stack
   :language: cpp

   //Example of the toStr function using a stack instead of recursion.

   #include <iostream>
   #include <string>
   #include <stack>
   using namespace std;

   stack<char> rStack;

   string toStr(int n, int base) {
       string convertString = "0123456789ABCDEF";
       while (n > 0) {
           if (n < base) {
               rStack.push(convertString[n]); //pushes string n to the stack
           } else {
               rStack.push(convertString[n % base]); //pushes string n modulo base to the stack.
           }
           n = n/base;
       }
       string res;
       while (!rStack.empty()) {
           //combines all the items in the stack into a full string.
           res = res + (string(1,  rStack.top()));
           rStack.pop();
       }
       return res;
   }

   int main() {
     cout << toStr(1453, 16);
   }