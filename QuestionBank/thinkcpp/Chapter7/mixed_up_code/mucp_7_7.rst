.. parsonsprob:: mucp_7_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: mixed_up_code
   :topics: Chapter7/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :practice: T

   Deep in the forest live the 7 dwarves named Sorty, Torty, Vorty,
   Worty, Xorty, Yorty, and Zorty. The program below should print
   out each of their names but the code is mixed up and contains extra blocks.
   Put the necessary blocks in the correct order.
   -----
   int main() {
   =====d
      string name = “Sorty”; #distractor
   =====
      string suffix = "orty";
   =====
      char letter = 'S';
   =====
      while (letter <= 'Z') {
   =====
         if (letter != 'U') {
   =====
         if (letter == 'U') {  #paired
   =====
         cout << letter + suffix << endl;
         }
   =====
         letter++;
      }
   }
   =====
         suffix++;  #paired
      }
   }