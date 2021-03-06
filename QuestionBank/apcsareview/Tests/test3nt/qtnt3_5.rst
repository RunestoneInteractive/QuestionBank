.. mchoice:: qtnt3_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :answer_e: 5
   :correct: c
   :feedback_a: 30 would not have been located in 1 iteration of the while loop. After one iteration, low would equal 0, mid would equal 3, and high would equal 7. Because list[3] is equal to 11, not 30, nothing is returned, low becomes 4, and the while-loop continues.
   :feedback_b: 30 would not have been located in 2 iterations of the while loop. After two iterations, mid would equal 5. Because list[5] is equal to 24, not 30, low would increase, and the while-loop would run again. Try one more iteration of the while loop.
   :feedback_c: 30 would be found in 3 iterations. After the third iteration of the while loop, mid would equal 6. list[6] equals 30, so 6 is returned and the while-loop is exited.
   :feedback_d: 4 iterations is too many iterations. Only 3 iterations are needed to find 30 in the array. After 4 iterations for an array with 7 elements, either the key is not present in the array or the key is at the first or last index of the array.
   :feedback_e: Only 3 iterations of the while loop are needed to find 30 in the array. After 5 iterations for an array with seven elements, it must be that the key was not found.

   Consider the following method ``binSearch``, which uses binary search to locate an element ``key`` in an array of integers ``arr``. If ``list`` is an array of integers containing ``{4, 7, 9, 11, 20, 24, 30, 41}``, how many iterations of the while loop occur in ``binSearch(30, list)``?

   .. code-block:: java

      public static int binSearch(int key, int[] arr)
      {
          int low = 0;
          int high = arr.length - 1;

          while (low <= high)
          {
              int mid = (low + high) / 2;

              if (arr[mid] == key)
                  return mid;

              else if (arr[mid] < key)
                  low = mid + 1;

              else
                  high = mid - 1;
          }

         return -1;
      }