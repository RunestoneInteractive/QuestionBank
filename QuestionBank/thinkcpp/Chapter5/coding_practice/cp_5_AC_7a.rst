.. activecode:: cp_5_AC_7a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: coding_practice
   :topics: Chapter5/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   bool isLeapYear (int year) {
       if (year % 400 == 0) {
           return true;
       }
       else if (year % 100 == 0) {
           return false;
       }
       else if (year % 4 == 0) {
           return true;
       }
       else {
           return false;
       }
   }

   int main() {
       cout << isLeapYear (2001) << endl;   // Should output 0
       cout << isLeapYear (2004) << endl;   // Should output 1
       cout << isLeapYear (2100) << endl;   // Should output 0
       cout << isLeapYear (2000) << endl;   // Should output 1
   }