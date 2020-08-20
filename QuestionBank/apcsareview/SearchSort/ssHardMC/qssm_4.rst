.. mchoice:: qssm_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: SearchSort
   :subchapter: ssHardMC
   :topics: SearchSort/ssHardMC
   :from_source: T
   :answer_a: 8,7,7,3,4,1
   :answer_b: 4,7,7,3,8,1
   :answer_c: 4,8,7,1,3,7
   :answer_d: 1,8,7,7,4,3
   :correct: b
   :feedback_a: This would be true if the array was not modified at all.
   :feedback_b: This is the correct answer. The for loop is iterating through every element in the array. The if statement is checking to see if the current element is even or odd. If it is even, then the first element of the array and the current element will swap places in the array.
   :feedback_c: This would be true if the loop had brought all the even numbers to the beginning of the array.
   :feedback_d: This would be true if the if statement had said: if(arr[i] % 2 == 1).

   What is printed when the following main method is executed?

   .. code-block:: java

          public class OddEvenMod
          {
              public static void main(String[] args)
              {
                  int[] arr = {8,7,7,3,4,1};
                  for (int i = 0; i < arr.length; i++)
                  {
                      if(arr[i] % 2 == 0)
                      {
                          int temp = arr[0];
                          arr[0] = arr[i];
                          arr[i] = temp;
                      }
                  }
                  for (int t = 0; t < arr.length; t++)
                  {
                      System.out.print((arr[t]) + ",");
                  }
              }
          }