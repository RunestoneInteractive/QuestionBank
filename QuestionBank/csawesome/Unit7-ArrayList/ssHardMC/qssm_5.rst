.. mchoice:: qssm_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssHardMC
   :topics: Unit7-ArrayList/ssHardMC
   :from_source: T
   :practice: T
   :answer_a: 3,5,3,9,2,4,
   :answer_b: 4,5,2,3,9,3,
   :answer_c: 5,3,2,9,3,4,
   :answer_d: 2,3,5,9,3,
   :correct: a
   :feedback_a: This is the correct answer. The check method is using a for loop and an if statement to return true if the parameter is prime and false if it is not prime. In the main method, the for loop iterates through every element in the array and checks to see if it is prime. If it is prime, then the program will swap that element with the first element in the array.
   :feedback_b: This would be true if the if statement had said: if(!check(arr[i])).
   :feedback_c: This would be true if the array had not been modified at all.
   :feedback_d: This would be true if the final for loop did not iterate through every element in the array.
   :pct_on_first: 0.3944315545
   :total_students_attempting: 862
   :num_students_correct: 814.0
   :mean_clicks_to_correct: 2.3611793612

   What is printed when the following main method is executed?
   
   .. code-block:: java
   
          public class PrimeOrNot
          {
              private static boolean check(int n)
              {
                  for(int i = 2; i < n; i++)
                  {
                      if(n % i == 0)
                          return false;
                  }
                  return true;
              }
   
              public static void main(String[] args)
              {
                  int[] arr = {5,3,2,9,3,4};
                  for (int i = 0; i < arr.length; i++)
                  {
                      if(check(arr[i]))
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