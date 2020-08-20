.. mchoice:: qtnt4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 5
   :answer_b: 6
   :answer_c: 8
   :answer_d: 13
   :answer_e: 15
   :correct: a
   :feedback_a: fibonacci(5) returns fibonacci(4) + fibonacci(3). fibonacci(4) returns fibonacci(3) and fibonacci(2). fibonacci(3) returns fibonacci(2) + fibonacci(1). fibonacci(2) returns fibonacci(1) + fibonacci(0). fibonacci(1) returns 1, and fibonacci(0) returns 0. When the code is traced, 5 is returned.
   :feedback_b: Check your tracing to make sure that fibonacci(0) returned 0 and fibonacci(1) returned 1.
   :feedback_c: This is the answer returned for fibonacci(6). Check your tracing and try again.
   :feedback_d: This is the answer returned for fibonacci(7). Check your tracing and try again.
   :feedback_e: Notice what is returned in the if statement. fibonacci(0) returns 0, not 1.
   :pct_on_first: 0.33
   :total_students_attempting: 100
   :num_students_correct: 98.0
   :mean_clicks_to_correct: 3.0

   The ``fibonacci`` method is shown below. What is returned as a result of ``fibonacci(5)``?
   
   .. code-block:: java
   
      public int fibonacci (int num)
      {
          if (num <= 1)
              return num;
   
          else
              return fibonacci(num - 1) + fibonacci(num - 2);
      }