.. mchoice:: qsearchsm_5
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ssMedMC
   :from_source: T
   :practice: T
   :answer_a: -1
   :answer_b: 0
   :answer_c: 1
   :answer_d: 2
   :answer_e: The code will not compile
   :correct: e
   :feedback_a: This would be true if the sequential search code was okay and v was a value that wasn't in the array, but the code is incorrect.  The <code>return -1</code> should be outside of the for loop.
   :feedback_b: This would be true if v was 1 and the code was correct for a sequential search.
   :feedback_c: This would be true if v was 2 and the code was correct for a sequential search.
   :feedback_d: This would be true if the code was correct for a sequential search, but it returns -1 inside the for loop instead of outside of it.
   :feedback_e: This method won't compile because it is supposed to return an integer and if the for loop doesn't execute it will not return anything.  The <code>return -1</code> should be outside the for loop to make this sequential search work as intended.

   What would test return if a = {1,2,3,4} and v =  3?

   .. code-block:: java

      public static int test(int[] a, int v)
      {
          for (int i = 0; i < a.length; i++)
          {
              if (a[i] == v)
                  return i;
              else return -1;
          }
      }