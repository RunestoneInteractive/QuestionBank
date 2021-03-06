.. mchoice:: qch_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: Exercises
   :topics: Unit3-If-Statements/Exercises
   :from_source: F
   :practice: T
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
   :pct_on_first: 0.2708481825
   :total_students_attempting: 1403
   :num_students_correct: 1381.0
   :mean_clicks_to_correct: 2.4742939899

   The following method will return true if and only if:
   
   .. code-block:: java
   
     public boolean check(String s) {
        return s.length() >= 2 && (s.charAt(0) ==
           s.charAt(1) || check(s.substring(1)));
     }