.. mchoice:: qtnt1_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: First: 15 Last: 29
   :answer_b: First: 15 Last: 30
   :answer_c: First: 16 Last: 29
   :answer_d: First: 16 Last: 30
   :answer_e: First: 16 Last: 28
   :correct: d
   :feedback_a: We add 1 to value before actually printing it, so the first value printed will be 16. The last time through the loop the value will be 29 (less than 30) but then the code will add one so it will print 30.
   :feedback_b: We add 1 to value before actually printing it, so the first value printed will be 16.
   :feedback_c: The last time through the loop the value will be 29 (less than 30) but then the code will add one so it will print 30.
   :feedback_d: The code adds one to value before the value is printed so 16 will be the first value printed.   The last time through the loop the value will be 29 (less than 30) but then the code will add one so it will print 30.
   :feedback_e: The last time through the loop the value will be 29 (less than 30) but then the code will add one so it will print 30.
   :pct_on_first: 0.5132978723
   :total_students_attempting: 376
   :num_students_correct: 373.0
   :mean_clicks_to_correct: 1.8418230563

   Consider the following block of code. What are the first and last numbers printed after running the code?
   
   .. code-block:: java
   
      int value = 15;
      while (value < 30)
      {
          value++;
          System.out.println(value);
      }