.. parsonsprob:: functions_p7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: mixedUpCode
   :topics: Chapter3/mixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Construct a function that takes a dollar amount and cent amount
   and prints the total amount of money that you have. Hint:
   the mod operator '%' returns the remainder of a division.
   -----
   void printAmount (int dollars, int cents) {
   =====
    int dollarTotal = dollars + cents / 100;
   =====
    double dollarTotal = dollars + cents / 100.0; #paired
   =====
    double centTotal = cents % 100;
   =====
    double centTotal = cents / 100; #paired
   =====
    cout << "$" << dollarTotal << "." << centTotal;
   =====
    cout << "$" << dollarTotal << centTotal; #paired
   =====
   }