.. mchoice:: qtnt3_16
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: When the length of str is less than 15
   :answer_b: When the length of str is greater than or equal to 15
   :answer_c: When the length of str is equal to 0
   :answer_d: For all string inputs
   :answer_e: For no string inputs
   :correct: e
   :feedback_a: If the string length is less than 15, "s" will be printed, but the recursive call will still be made.
   :feedback_b: This would be correct if the recursive call was located in an else statement. If the string length is 15 or greater, "s" will not be printed, but the recursive call will still occur.
   :feedback_c: If the string has length 0, the if statement will occur and "s" will be printed, but the recursive call will still occur.
   :feedback_d: Check the recursive call. The method is always called recursively, regardless of the string length.
   :feedback_e: There is no base case present in this method that stops the recursive calls. This method will continue until the compiler runs out of memory. You could fix this code by placing the recursive call in an else statement or creating a base case to end the call.
   :pct_on_first: 0.2389380531
   :total_students_attempting: 113
   :num_students_correct: 109.0
   :mean_clicks_to_correct: 2.7981651376

   
   The method ``recur`` is shown below. In which case will ``recur`` terminate without error?
   
   .. code-block:: java
   
      public void recur (String str)
      {
           if (str.length() < 15)
               System.out.print("s");
   
           recur(str + "!");
      }