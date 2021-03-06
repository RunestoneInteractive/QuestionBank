.. mchoice:: qtnt1_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: It will never produce a run time error.
   :answer_b: It will always produce a run time error.
   :answer_c: Only when the length of the input string is greater than or equal to 16.
   :answer_d: Only when an empty string is input.
   :answer_e: Whenever the input string length is less than 16.
   :correct: b
   :feedback_a: Since there is no terminating condition surrounding our recursive method call (because the call lies outside of the if statement), it will keep doing recursive calls until we eventually get a run time error.
   :feedback_b: Since there is no statement that terminates the recursive call to stringRecursion (the length of the string s will increase until it is greater than 16, but the recursive call will keep happening because the recursive call is outside the if statement) the computer will keep doing recurisve calls until it runs out of memory and a run time error will happen.
   :feedback_c: Since the recursive call is outside the condition and the conditional doesn't include a return then this will result in infinite recursion and eventually a run time error.
   :feedback_d: The length of the string will not matter in this case because the recursive call to stringRecursion will always happen, since the recursive call lies outside the body of the conditional. The string length will only determine if the string s is printed out to the console or not.
   :feedback_e: We will get run time errors regardless of the length of the string s. This is due to the fact that the recursive call lies outside the body of the conditional. If the length of the string s is less than 16 then we will get something printed out to the console until the length of s becomes greater than 16, and then we will continue in a infinite recursion.
   :pct_on_first: 0.2338028169
   :total_students_attempting: 355
   :num_students_correct: 353.0
   :mean_clicks_to_correct: 2.6288951841

   When will the method ``stringRecursion`` produce a run time error?
   
   .. code-block:: java
   
      public void stringRecursion(String s)
      {
   
        if (s.length() < 16)
        {
          System.out.println(s);
        }
        stringRecursion(s + "*");
      }