.. mchoice:: qse_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: 3
   :answer_b: 4
   :answer_c: 5
   :answer_d: -1
   :correct: a
   :feedback_a: The method indexOf returns the first position of the passed str in the current string starting from the left (from 0).
   :feedback_b: The first character is at index 0 in a string, not 1.
   :feedback_c: Does the indexOf method find the first occurrence of the character, or the last?
   :feedback_d: Does the string contain a d?  The pos method will return the first index that the character is at in the string.
   :pct_on_first: 0.6739620212
   :total_students_attempting: 3107
   :num_students_correct: 3074.0
   :mean_clicks_to_correct: 1.5787247885

   What is the value of pos after the following code executes?
   
   .. code-block:: java
   
     String s1 = "ac ded ca";
     int pos = s1.indexOf("d");