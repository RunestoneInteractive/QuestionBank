.. parsonsprob:: mucp_5_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: mixed_up_code
   :topics: Chapter5/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   When you buy something, you also need to pay sales tax. For example,
   a nice shirt could be labeled with a price of exactly $20, but when
   you pay, you actually need to pay $21.20 in a state with 6% sales tax.
   However, different states have different tax rates. Write the function
   ``priceWithTax``, which takes two ``double``\s, ``price`` and ``percentTax``.
   ``priceWithTax`` calculates the price after tax and returns a ``double``.
   For example, ``priceWithTax (20, 6)`` returns 21.2.
   Put the necessary blocks of code in the correct order.
   -----
   double priceWithTax (double price, double percentTax) {
   =====
   int priceWithTax (double price, int percentTax) {  #distractor
   =====
   double priceWithTax (price, percentTax) {  #distractor
   =====
      return (1 + percentTax / 100) * price;
   =====
      return (1 + percentTax) * price;  #distractor
   =====
      return percentTax * price;  #distractor
   =====
   }