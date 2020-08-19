.. mchoice:: qrh_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rHardMC
   :topics: Unit10-Recursion/rHardMC
   :from_source: T
   :practice: T
   :answer_a: The string <code>s</code> contains two or more of the same characters.
   :answer_b: The string <code>s</code> starts with two or more of the same characters.
   :answer_c: The string <code>s</code> contains two or more of the same character that are next to each other.
   :answer_d: The string <code>s</code> ends with two or more of the same characters
   :correct: c
   :feedback_a: It is not enough for <code>s</code> to contain two of the same characters, they must be adjacent to satisfy <code>s.charAt(0) == s.charAt(1)</code>.
   :feedback_b: It is not neccessary for the adjacent characters to be at the start of the string.
   :feedback_c: This method will return true when <code>s</code> has at least 2 characters in it and at least 2 characters are the same and are adjacent.
   :feedback_d: It is not neccessary for the adjacent characters to be at the end of the string.
   :pct_on_first: 0.5235955056
   :total_students_attempting: 445
   :num_students_correct: 439.0
   :mean_clicks_to_correct: 1.7562642369

   Given the following method declaration, this method will return true if and only if:
   
   .. code-block:: java
   
      public static boolean check(String s)
      {
         return s.length() >= 2 &&
                (s.charAt(0) == s.charAt(1) ||
                 check(s.substring(1)));
      }