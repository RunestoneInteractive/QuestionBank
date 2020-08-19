.. mchoice:: qssm_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssHardMC
   :topics: Unit7-ArrayList/ssHardMC
   :from_source: T
   :practice: T
   :answer_a: 6 7 17 3 2 9 1 5
   :answer_b: 9 6 3 2 3 1 5 17
   :answer_c: 5 1 2 3 6 17 7 9
   :answer_d: 9 7 17 6 3 2 1 5
   :correct: d
   :feedback_a: This would be true if the program had not modified the array at all.
   :feedback_b: This would be true if the loop was moving the position of odd numbers in the array to arr.length-1.
   :feedback_c: This would be true if the array was printed in the reversed order.
   :feedback_d: This is the correct answer, because the divCheck method is checking to see if the values in the array are divisible by 2 or 3. If they are, they are swapped with the value at the first position (index 0).
   :pct_on_first: 0.3424494649
   :total_students_attempting: 841
   :num_students_correct: 792.0
   :mean_clicks_to_correct: 2.125

   What is printed when the following main method is executed?
   
   .. code-block:: java
   
          public class DivisibleBy2or3
          {
              private static boolean divCheck(int n)
              {
                  if(n % 2 == 0 || n % 3 == 0)
                  {
                    return true;
                  }
                  return false;
              }
   
              public static void main(String[] args)
              {
                  int[] arr = {6,7,17,3,2,9,1,5};
                  for (int i = 0; i < arr.length; i++)
                  {
                      if(divCheck(arr[i]))
                      {
                          int temp = arr[0];
                          arr[0] = arr[i];
                          arr[i] = temp;
                      }
                  }
                  for (int t = 0; t < arr.length; t++)
                  {
                      System.out.print((arr[t]) + " ");
                  }
              }
          }