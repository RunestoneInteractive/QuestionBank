.. mchoice:: qssm_1
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ssHardMC
   :from_source: T
   :practice: T
   :answer_a: A B B C D
   :answer_b: E D C B B A
   :answer_c: A B B C D E
   :answer_d: E D C B A B
   :answer_e: E D C B B
   :correct: c
   :feedback_a: This would be true if the for loop inside the main method did not interate through every value in the array.
   :feedback_b: This would be true if the conditional statement inside the for loop stated "if (key.compareTo(letters[i]) < 0)", because that would put the array in a reverse alphabetical order.
   :feedback_c: This is an insertion sort which sorts the array in alphabetical order using the compareTo() method.
   :feedback_d: This would be true if array was not modified at all in the main method.
   :feedback_e: This would be true if the conditional statement inside the for loop stated "if (key.compareTo(letters[i]) < 0)" and if the loop did not iterate through every item of the letters array, because that would put the array in a reverse alphabetical order.

   What is printed when the following main method is executed? The break; statement used in this code breaks out of or terminates the loop at that point. It is not used on the AP CS A exam.

   .. code-block:: java

      public class AlphaSort
      {

          public static void main(String[] args)
          {
              int i, j;
              String key;
              String[] letters = {"E","D","C","B","A","B"};
              for (j = 1; j < letters.length; j++)
              {
                  key = letters[j];
                  i = j - 1;
                  while (i >= 0)
                  {
                      if (key.compareTo(letters[i]) > 0)
                      {
                          break;
                      }
                      letters[i + 1] = letters[i];
                      i--;
                  }
                  letters[i + 1] = key;
              }
              for (int t = 0; t < letters.length; t++)
              {
                  System.out.print((letters[t]) + "");
              }
          }
      }