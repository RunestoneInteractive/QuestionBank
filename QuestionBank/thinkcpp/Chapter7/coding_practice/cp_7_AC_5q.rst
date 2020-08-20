.. activecode:: cp_7_AC_5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: coding_practice
   :topics: Chapter7/coding_practice
   :from_source: T
   :language: cpp
   :practice: T

   #include <iostream>
   #include "ctype.h"
   using namespace std;

   string ROT13 (string input) {
       // Write your implementation here.
   }

   int main() {
       string original = "Encrypt me then decrypt me!";
       string encrypted = ROT13 (original);
       string decrypted = ROT13 (encrypted);
       cout << original << endl;
       cout << encrypted << endl;
       cout << decrypted << endl;

       // Uncomment and run the code below once your function works!
       // string secretMessage = "Pbatenghyngvbaf! Lbh'ir fhpprffshyyl vzcyrzragrq EBG13 naq qrpbqrq gur frperg zrffntr :)";
       // cout << ROT13 (secretMessage) << endl;
   }