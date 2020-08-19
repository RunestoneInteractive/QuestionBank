.. mchoice:: qpret_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit1-Getting-Started
    :subchapter: ptest1
    :topics: Unit1-Getting-Started/ptest1
    :from_source: F
    :answer_a: It is the length of the array nums.
    :answer_b: It is the length of the first consecutive block of the value target in nums.
    :answer_c: It is the number of occurrences of the value target in nums.
    :answer_d: It is the length of the shortest consecutive block of the value target in nums.
    :answer_e: It is the length of the last consecutive block of the value target in nums.
    :correct: c
    :feedback_a: This can not be true. There is no nums.length in the code and the only count happens lenCount is incremented when nums[k] == target.
    :feedback_b: It does not reset the count ever so it just counts all the times the target value appears in the array.
    :feedback_c: The variable lenCount is incremented each time the current array element is the same value as the target. It is never reset so it counts the number of occurrences of the value target in nums. The method returns maxLen which is set to lenCount after the loop finishes if lenCount is greater than maxLen.
    :feedback_d: It does not reset the count ever so it just counts all the times the target value appears in the array.
    :feedback_e: It does not reset the count ever so it just counts all the times the target value appears in the array.

        Consider the following data field and method ``findLongest``. Method ``findLongest`` is intended to find the longest consecutive block of the value target occurring in the array nums; however, ``findLongest`` does not work as intended. For example, if the array nums contains the values [7, 10, 10, 15, 15, 15, 15, 10, 10, 10, 15, 10, 10], the call ``findLongest(10)`` should return 3, the length of the longest consecutive block of 10s.  Which of the following best describes the value returned by a call to ``findLongest``?

        .. code-block:: java

            private int[] nums;
            public int findLongest(int target)
            {
               int lenCount = 0;
               int maxLen = 0;

               for (int k = 0; k < nums.length; k++)
               {
                  if (nums[k] == target)
                  {
                     lenCount++;
                  }

                  else
                  {
                     if (lenCount > maxLen)
                     {
                        maxLen = lenCount;
                     }
                 }
               }

               if (lenCount > maxLen)
               {
                  maxLen = lenCount;
               }

               return maxLen;
            }