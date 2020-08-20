.. parsonsprob:: vars_types_p9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: mixedUpCode
   :topics: Chapter2/mixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   It's Black Friday and the game system you'be been saving up for is marked
   down to 60% of its original price!  Construct a block of code that calculates
   how much money you'd be saving if the system originally costed $359.99?
   
   -----
   int main() {
   =====
    double game = 359.99;
   =====
    double game = $359.99; #paired
   =====
    int game = 359.99; #paired
   =====
    double discountGame = game * 0.60;
   =====
    double discountGame = game / 0.60; #paired
   =====
    double moneySaved = game - discountGame;
   =====
    double moneySaved = discountGame; #paired
   =====
    double moneySaved = game + discountGame; #paired
   =====
   }