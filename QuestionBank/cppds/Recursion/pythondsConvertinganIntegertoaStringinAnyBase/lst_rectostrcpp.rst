.. activecode:: lst_rectostrcpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
   :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
   :from_source: T
   :caption: Recursively Converting from  Integer to String
   :language: cpp

   //Recursive example of converting from int to string.

   #include <iostream>
   #include <string>
   using namespace std;

   string toStr(int n, int base) {
       string convertString = "0123456789ABCDEF";
       if (n < base) {
           return string(1, convertString[n]); // converts char to string, and returns it
       } else {
           return toStr(n/base, base) + convertString[n%base]; // function makes a recursive call to itself.
       }
   }

   int main() {
     cout << toStr(1453, 16);
   }