.. mchoice:: printTime_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: printTime
   :topics: Chapter9/printTime
   :from_source: T
   :answer_a: cout << "Price is " << "p.dollar" << " dollars and" << "p.cents" << "cents." << endl;
   :answer_b: cout << "Price is " << p.dollar << " dollars and " << p.cents << " cents." << endl;
   :answer_c: cout << "Price is " << p.dollar << " dollars and " << p.cents << "cents." << endl
   :correct: b
   :feedback_a: Try again.
   :feedback_b: Correct!
   :feedback_c: There is an important character that ends nearly all statements in C++.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Which of the following would be a correct way to display the price of an object and finish the ``printPrice``, which we saw on the previous page?
   
   .. code-block:: cpp
   
      struct Price {
        int dollar, cents;
      };
   
      void printPrice(Price& p) {
        // Implementation here
      }
   
      int main() {
        Price sandwich = { 3, 45 };
        Price coffee = { 2, 50 };
        Price pastry = { 2, 0 };
      }