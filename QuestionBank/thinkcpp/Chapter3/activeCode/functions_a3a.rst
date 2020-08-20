.. activecode:: functions_a3a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: activeCode
   :topics: Chapter3/activeCode
   :from_source: T
   :language: cpp

   Below is one way to fix the program.  It's crucial that
   you input your arguments in the correct order so as to
   avoid a semantic error.  Also, it's important that you
   understand that when you divide two integers... you will
   get an integer as a result.
   ~~~~
   #include <iostream>
   using namespace std;

   void divide (double a, double b) {
       cout << a / b;
   }

   int main () {
       int a = 8;
       int b = 12;
       cout << b << " / " << a << " = ";
       divide (b, a);
   }