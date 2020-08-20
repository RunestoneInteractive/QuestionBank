.. parsonsprob:: mucp_6_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: mixed_up_code
   :topics: Chapter6/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   The program below should print out the even numbers between 20 and 40
   but the code is mixed up and contains extra blocks. Put the necessary blocks
   in the correct order.
   -----
   int main() {
   =====
   main(int) {                         #paired
   =====
      int n = 20;
   =====
      int n = 0; #distractor
   =====
      while (n <= 40) {
   =====
      while (n < 40) {                        #paired
   =====
         cout << n << endl;
   =====
         n = n + 2;
      }
   }
   =====
         n++;                 #distractor
      }
   }
   =====
         n = n * 2;                 #distractor
      }
   }