.. mchoice:: qtnt2_19
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III and IV only
   :answer_d: I and II only
   :answer_e: II and IV only
   :correct: a
   :feedback_a: The modulus operator (%) can be used to find if numbers are even or odd. I checks that x is even correctly using x % 2 == 0.
   :feedback_b: II uses the modulus operator to count the number of odd numbers in the array. If x % 2 == 1, then the number is odd, not even.
   :feedback_c: III and IV use the division operator, not the modulus operator. This does not check if the number is even.
   :feedback_d: I is correct, but II increments the counter for odd numbers, not even numbers.
   :feedback_e: II counts the odd numbers instead of the even numbers. If x % 2 == 1, the number is odd, not even. IV does not use the modulus operator (%), which checks if numbers are even or odd.


   Consider the following method ``evens``, which finds the number of even numbers present in an array. Which of the following segments of code would correctly replace ``/* to be completed */``?

   .. code-block:: java

     public int evens(int [] arr)
     {
        int count = 0;

        for (int x : arr)
        {
           /* to be completed */
        }

        return count;
     }

     // I
     if (x % 2 == 0)
        count++;

     // II
     if (x % 2 == 1)
        count++;

     // III
     if (x / 2 == 0)
        count++;

     // IV
     if (x / 2 == 1)
        count++;