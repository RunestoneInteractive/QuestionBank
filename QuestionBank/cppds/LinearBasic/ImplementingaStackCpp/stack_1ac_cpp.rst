.. activecode:: stack_1ac_cpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: LinearBasic
   :subchapter: ImplementingaStackCpp
   :topics: LinearBasic/ImplementingaStackCpp
   :from_source: T
   :caption: Using the Stack methods from the STL in C++
   :language: cpp


   //Tests the push, empty, size, pop, and top methods of the stack library.

   #include <iostream>
   #include <stack>    // Calling Stack from the STL

   using namespace std;

   int main() {
       stack<int> newStack;

       newStack.push(3); //Adds 3 to the stack
       newStack.push(8);
       newStack.push(15);

       // returns a boolean response depending on if the stack is empty or not
       cout << "Stack Empty? " << newStack.empty() << endl;

       // returns the size of the stack itself
       cout << "Stack Size: " << newStack.size() << endl;

       // returns the topmost element of the stack
       cout << "Top Element of the Stack: " << newStack.top() << endl;

       // removes the topmost element of the stack
       newStack.pop();

       cout << "Top Element of the Stack: " << newStack.top() << endl;

       cout << "Stack Size: " << newStack.size() << endl;

       return 0;
   }