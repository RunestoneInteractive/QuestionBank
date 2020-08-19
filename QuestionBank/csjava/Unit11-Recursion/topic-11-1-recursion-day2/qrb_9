.. mchoice:: qrb_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit11-Recursion
   :subchapter: topic-11-1-recursion-day2
   :topics: Unit11-Recursion/topic-11-1-recursion-day2
   :from_source: T
   :practice: T
   :answer_a: 7
   :answer_b: 2
   :answer_c: 1
   :answer_d: 3
   :answer_e: 0
   :correct: b
   :feedback_a: This would be correct if was counting the number of characters in the string, but that isn't what it is doing.
   :feedback_b: This method seems to be counting the number of y's in the string, but fails to check if a single character is a y.
   :feedback_c: Don't forget that there are recursive calls too.
   :feedback_d: This would be correct if the base case returned 1 if the single character was a y.
   :feedback_e: Don't forget about the recursive calls.

        Given the method defined below what does the following return: mystery("xyzxyxy")? Note that this recursive method traverses a String.

    .. code-block:: java
     :linenos:

     public static int mystery(String str)
     {
        if (str.length() == 1) return 0;
        else
        {
           if (str.substring(0,1).equals("y")) return 1 +
                                mystery(str.substring(1));
           else return mystery(str.substring(1));
        }
     }