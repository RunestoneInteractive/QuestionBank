.. activecode:: cp_6_AC_9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: coding_practice
   :topics: Chapter6/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   int main() {
       int first = 0;
       int second = 1;
       int third;
       int n = 2;
       cout << first << " " << second << " ";
       while (n < 20) {
           third = first + second;
           cout << third << " ";
           first = second;
           second = third;
           n++;
       }
   }