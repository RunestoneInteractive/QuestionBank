.. mchoice:: qrm_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rMedMC
   :topics: Unit10-Recursion/rMedMC
   :from_source: T
   :practice: T
   :answer_a: 1441
   :answer_b: 43211234
   :answer_c: 3443
   :answer_d: 12344321
   :answer_e: Many digits are printed due to infinite recursion.
   :correct: b
   :feedback_a: The first call to <code>mystery</code> with the integer 1234 will print 1234 % 10. The '%' means modulo or remainder. The remainder of 1234 divided by 10 is 4 so the first thing printed must be 4.
   :feedback_b: This has a recursive call which means that the method calls itself when (x / 10) is greater than or equal to zero. Each time the method is called it prints the remainder of the passed value divided by 10 and then calls the method again with the result of the integer division of the passed number by 10 (which throws away the decimal part). After the recursion stops by <code>(x / 10) == 0</code> the method will print the remainder of the passed value divided by 10 again.
   :feedback_c: The first call to <code>mystery</code> with the integer 1234 will print 1234 % 10. The '%' means modulo or remainder. The remainder of 1234 divided by 10 is 4 so the first thing printed must be 4.
   :feedback_d: The first call to <code>mystery</code> with the integer 1234 will print 1234 % 10. The '%' means modulo or remainder. The remainder of 1234 divided by 10 is 4 so the first thing printed must be 4.
   :feedback_e: When the recursive call to <code>mystery(1)</code> occurs (the 4th call to mystery), the division of x /10 equals .01--this becomes 0 because this is integer division and the remainder is thrown away. Therefore the current call will be completed and all of the previous calls to <code>mystery</code> will be completed.
   :pct_on_first: 0.6427145709
   :total_students_attempting: 501
   :num_students_correct: 494.0
   :mean_clicks_to_correct: 1.6639676113

   Given the following method declaration, which of the following is printed as the result of the call ``mystery(1234)``?
   
   .. code-block:: java
      :linenos:
   
      //precondition:  x >=0
      public static void mystery (int x)
      {
         System.out.print(x % 10);
   
         if ((x / 10) != 0)
         {
            mystery(x / 10);
         }
         System.out.print(x % 10);
      }