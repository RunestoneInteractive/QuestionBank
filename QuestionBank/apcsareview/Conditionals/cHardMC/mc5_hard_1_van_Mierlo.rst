.. mchoice:: mc5_hard_1_van_Mierlo
   :author: Matthijs van Mierlo
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cHardMC
   :topics: Conditionals/cHardMC
   :from_source: F
   :answer_a: s starts with two or more of the same characters
   :answer_b: s contains two or more of the same characters
   :answer_c: s contains two or more of the same character in a row
   :answer_d: s ends with two or more of the same characters
   :answer_e: s.charAt(0) == s.charAt(1)
   :correct: c
   :feedback_a: It is not neccessary for the adjoining characters to be at the start of the string.
   :feedback_b: The character must be adjoining in order to satisfy the s.charAt(0) == s.charAt(1) portion of the return statement.
   :feedback_c: This will return true when s has at least 2 characters in it and at least 2 characters are the same in a row.
   :feedback_d: It is not neccessary for the adjoining characters to be at the end of the string.
   :feedback_e: This returns true whenever there are at least 2 of the same character in a row in the string. It does this because of the recursive call. So, the first two characters don't have to be the ones that are the same.

   The following method will return true if and only if:

   .. code-block:: java

     public boolean check(String s) {
        return s.length() >= 2 && (s.charAt(0) == s.charAt(1) || check(s.substring(1)));
     }