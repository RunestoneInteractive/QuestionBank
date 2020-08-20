.. mchoice:: qtnt4_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :answer_e: 5
   :correct: c
   :feedback_a: This would be the correct answer if sequential search is used. Remember that the loop will continue until a value is returned or the value is not found, regardless of the position of key.
   :feedback_b: Remember that even if low and high are equal, the while loop will still continue to compare a value.
   :feedback_c: After the first instance of the while loop, high = 7 and mid = 3. Because intArr[3] is greater than 5, high becomes 2, mid becomes 1, and the loop passes again. intArr[2] is also greater than 5, so high becomes 0, mid becomes 0, and the loop passes again. intArr[0] equals 5, so the key was found in three iterations of the while-loop.
   :feedback_d: This number is too high for a binary search algorithm. There are 8 elements in the array, and binary search uses, at a maximum, log2 (number of elements) iterations. log2 (8) is less than 4.
   :feedback_e: This number is too high for a binary search algorithm. There are 8 elements in the array, and binary search uses, at a maximum, log2 (number of elements) iterations. log2 (8) is less than 5.

   Consider the ``binSearch`` method shown below, which uses a binary search algorithm to locate an integer ``key`` in an array. Assume ``intArr`` is an array of integers containing ``[5, 7, 9, 11, 21, 29, 36, 45]``. How many iterations of the while loop occur in ``binSearch(5, intArr)``?

   .. code-block:: java

      public int binSearch(int key, int[] arr)
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