.. mchoice:: qtnt2_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: 1
   :answer_b: 0
   :answer_c: 10 9 8 7 6 5 4 3 2 1
   :answer_d: 1 2 3 4 5 6 7 8 9 10
   :answer_e: 10
   :correct: a
   :feedback_a: After the recursive call reaches the base case (where arg = 1), the compiler prints "1". The recursive calls all just return and don't print anything.
   :feedback_b: This would be correct if the recursive call specified that arg >= 1 or arg > 0. Because the code ends when arg reaches a value of 1, the code will not print out 0.
   :feedback_c: This would be correct if the method printed out arg + " " before going to the recursive call. Because the print statement is located at the end of the base case and not the recursive call, not every value is printed.
   :feedback_d: This would be correct if the method printed arg + " " after the recursive call in the if statement. Because the method does not return any values or strings, and because only the base case has a print statement, only the last value of arg is printed.
   :feedback_e: This would be correct if the method returned an integer that was the sum of the previous calls. The method does not add any values.
   :pct_on_first: 0.4525139665
   :total_students_attempting: 179
   :num_students_correct: 177.0
   :mean_clicks_to_correct: 2.4971751412

   Consider the class ``showMe``, shown below. What is printed as a result of ``showMe(10)``?
   
   .. code-block:: java
   
      public static void showMe(int arg)
      {
         if (arg > 1)
         {
            showMe(arg - 1);
         }
   
         else
         {
            System.out.print(arg + " ");
         }
      }