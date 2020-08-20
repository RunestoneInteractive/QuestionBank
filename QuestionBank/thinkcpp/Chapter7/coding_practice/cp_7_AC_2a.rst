.. activecode:: cp_7_AC_2a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: coding_practice
   :topics: Chapter7/coding_practice
   :from_source: F
   :language: cpp

   #include <iostream>
   #include "ctype.h"
   using namespace std;

   void stringToLower (string &input) {
       int i = 0;
       while (i < input.length()) {
           if (isalpha(input[i]) && isupper(input[i])) {
               input[i] = tolower(input[i]);
           }
           i++;
       }
   }

   int countWord (string input, string word) {
       stringToLower (input);
       int count = 0;
       while ((int)input.find(word) != -1) {
           count++;
           input = input.substr(input.find(word) + word.length());
       }
       return count;
   }

   int main() {
       string quote =
           "Anyway, like I was sayin', shrimp is the fruit of the sea. You can "
           "barbecue it, boil it, broil it, bake it, saute it. Dey's uh, "
           "shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, "
           "stir-fried. There's pineapple shrimp, lemon shrimp, coconut shrimp, "
           "pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and "
           "potatoes, shrimp burger, shrimp sandwich. That- that's about "
           "it.";
       cout << countWord(quote, "shrimp");    // There should be 14 instances of the word "shrimp"
   }