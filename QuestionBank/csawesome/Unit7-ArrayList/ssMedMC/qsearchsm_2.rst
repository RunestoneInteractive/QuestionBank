.. mchoice:: qsearchsm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssMedMC
   :topics: Unit7-ArrayList/ssMedMC
   :from_source: T
   :practice: T
   :answer_a: -1
   :answer_b: 0
   :answer_c: 1
   :answer_d: 2
   :answer_e: 3
   :correct: c
   :feedback_a: This would be true if the third value was something that wasn't in the array.
   :feedback_b: This would be true if the third value was 1
   :feedback_c: This is a binary search and it returns the index of the value 3, which is 1.
   :feedback_d: This would be true if the third value was 5.
   :feedback_e: This would be true if the third value was 8.
   :pct_on_first: 0.3693131133
   :total_students_attempting: 1121
   :num_students_correct: 1075.0
   :mean_clicks_to_correct: 2.303255814

   What is printed when the following main method is executed?
   
   .. code-block:: java
   
      public class Searcher
      {
          private int[] arr = {1,3,5,8,9};
   
          public int mystery(int low, int high, int num)
          {
              int mid = (low + high) / 2;
              if (low > high) {
                  return -1;   }
              else if (arr[mid] < num) {
                  return mystery(mid + 1, high, num);   }
              else if (arr[mid] > num) {
                  return mystery(low, mid - 1, num);   }
              else
                  return mid;
          }
   
          public static void main(String[] args)
          {
              Searcher s = new Searcher();
              System.out.println(s.mystery(0,4,3));
          }
      }