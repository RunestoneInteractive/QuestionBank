.. mchoice:: qsearchsm_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssMedMC
   :topics: Unit7-ArrayList/ssMedMC
   :from_source: T
   :practice: T
   :answer_a: int k = j - 1; k >= 0; k--
   :answer_b: int k = j + 1; k < elem.length; k++
   :answer_c: int k = j; k < elem.length; k++
   :answer_d: int k = j; k >= 0; k--
   :answer_e: int k = j - 1; k > 0; k--
   :correct: b
   :feedback_a: The inner loop starts at the outer loop value plus one, not minus one.
   :feedback_b: The inner loop starts at the outer loop value plus one and ends at the last element.
   :feedback_c: The inner loop should start at the outer loop value plus one.
   :feedback_d: The inner loop should start at the outer loop value plus one and increment.
   :feedback_e: The inner loop should start at the outer loop value plus one and increment.
   :pct_on_first: 0.4194690265
   :total_students_attempting: 1130
   :num_students_correct: 1081.0
   :mean_clicks_to_correct: 2.2192414431

   Which of the following could be used to replace // missing code // in the code so that the method always sorts the array ``elem`` in ascending order?
   
   .. code-block:: java
   
      public class Searcher
      {
   
          public static void sort(int[] elem)
                  {
              for (int j = 0; j < elem.length - 1; j++)
              {
                  int minIndex = j;
   
                  for (// missing code //)
                  {
                      if (elem [k] < elem [minIndex])
                      {
                          minIndex = k;
                      }
                  }
                  int temp = elem[j];
                  elem[j] = elem[minIndex];
                  elem[minIndex] = temp;
              }
          }
   
          public static void main(String[] args)
          {
              int[] nums = {28, -3, 2, 14, 30};
              Searcher.sort(nums);
          }
      }