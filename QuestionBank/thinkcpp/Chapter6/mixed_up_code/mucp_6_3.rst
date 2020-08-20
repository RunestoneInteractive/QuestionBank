.. parsonsprob:: mucp_6_3
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
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   The program below should find the sum of the first 10 natural numbers,
   but the code is mixed up and contains extra blocks. Put the necessary blocks
   in the correct order.
   -----
   int main() {
   =====
      int n = 1;
   =====
      int n = 10; #distractor
   =====
      int sum = 0;
   =====
      int sum = n;  #distractor
   =====
      while (n <= 10) {
   =====
      while (n < 100) {  #distractor
   =====
      while (n <= 9) {  #distractor
   =====
         cout << n << endl;  #distractor
   =====
         count = count + n;
   =====
         n++;
      }
   =====
   }