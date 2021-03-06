.. mchoice:: qamed_3
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: It is the length of the shortest consecutive block of the value <code>target</code>  in <code>nums</code>
   :answer_b: It is the length of the array <code>nums</code>
   :answer_c: It is the length of the first consecutive block of the value <code>target</code>  in <code>nums</code>
   :answer_d: It is the number of occurrences of the value <code>target</code>  in <code>nums</code>
   :answer_e: It is the length of the last consecutive block of the value <code>target</code>  in <code>nums</code>
   :correct: d
   :feedback_a: It doesn't reset <code>lenCount</code> ever, so it just counts all the times the <code>target</code> value appears in the array.
   :feedback_b: The only count happens when <code>lenCount</code> is incremented when <code>nums[k] == target</code>. <code>nums.length</code> is only used to stop the loop.
   :feedback_c: It doesn't reset <code>lenCount</code> ever, so it just counts all the times the <code>target</code> value appears in the array.
   :feedback_d: The variable <code>lenCount</code> is incremented each time the current array element is the same value as the <code>target</code>. It is never reset so it counts the number of occurrences of the value <code>target</code> in <code>nums</code>. The method returns <code>maxLen</code> which is set to <code>lenCount</code> after the loop finishes if <code>lenCount</code> is greater than <code>maxLen</code>.
   :feedback_e: It doesn't reset <code>lenCount</code> ever, so it just counts all the times the <code>target</code> value appears in the array.

   Consider the following data field and method ``findLongest``. Method ``findLongest`` is intended to find the longest consecutive block of the value ``target`` occurring in the array ``nums``; however, ``findLongest`` does not work as intended. For example given the code below the call ``findLongest(10)`` should return 3, the length of the longest consecutive block of 10s. Which of the following best describes the value actually returned by a call to ``findLongest``?

   .. code-block:: java

     private int[] nums = {7, 10, 10, 15, 15, 15, 15, 10, 10, 10, 15, 10, 10};

     public int findLongest(int target) {
        int lenCount = 0; // length of current consecutive numbers
        int maxLen = 0;   // max length of consecutive numbers
        for (int k = 0; k < nums.length; k++) {
           if (nums[k] == target) {
              lenCount++;
           } else if (lenCount > maxLen) {
              maxLen = lenCount;
           }
        }
        if (lenCount > maxLen) {
           maxLen = lenCount;
        }
        return maxLen;
     }