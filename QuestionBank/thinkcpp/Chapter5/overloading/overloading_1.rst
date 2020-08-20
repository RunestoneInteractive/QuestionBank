.. mchoice:: overloading_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: overloading
   :topics: Chapter5/overloading
   :from_source: T
   :answer_a: double price(int a, int b);
   :answer_b: double price(int a, string b, string c);
   :answer_c: double price(double x, int y, string z);
   :answer_d: all of the above
   :correct: b
   :feedback_a: This function has the same parameters as the first function below.
   :feedback_b: While this function has the same number of parameters as the second function, it takes different types of parameters.
   :feedback_c: This function has the same parameters as the second function below.
   :feedback_d: Take another look at the numbers and types of parameters.
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 3.0

   Which of the following function declarations would be legal if it was added to the program below?
   
   ::
   
       double price (int x, int y);
       double price (double a, int b, string c);