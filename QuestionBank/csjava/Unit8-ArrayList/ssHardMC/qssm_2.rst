.. mchoice:: qssm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: ssHardMC
   :topics: Unit8-ArrayList/ssHardMC
   :from_source: T
   :practice: T
   :answer_a: 4
   :answer_b: 2
   :answer_c: 12
   :answer_d: 1
   :correct: b
   :feedback_a: This would be true if the if statement was not trying to check if the numbers in the array were negative and odd.
   :feedback_b: This answer is correct because the for loop iterates through every element and increments the count if the current number is negative and odd.
   :feedback_c: This may be a result of misunderstanding the question, as 12 cannot be an answer because the array length itself is only 6.
   :feedback_d: This would be true if the code was looking for the numbers in the array that were positive and odd.

   What is printed when the following main method is executed?

   .. code-block:: java

      public class NumberCount
      {
          public static void main(String[] args)
          {
              int count = 0;
              int[] numbers = {-5,4,-5,3,-2,-4};
              for (int j = 0; j < numbers.length; j++)
              {
                  if(numbers[j] < 0 && numbers[j] % 2 != 0)
                  {
                      count++;
                  }
              }
          System.out.println(count);
          }
      }