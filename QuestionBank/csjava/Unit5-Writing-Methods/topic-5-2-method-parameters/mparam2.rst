.. mchoice:: mparam2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit5-Writing-Methods
   :subchapter: topic-5-2-method-parameters
   :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
   :from_source: F
   :practice: T
   :answer_a: mystery("abc", 9);
   :answer_b: mystery("xyz", "9");
   :answer_c: mystery(9, 5);
   :correct: a
   :feedback_a: The actual argument and formal parameter types match.
   :feedback_b: The second parameter i has type int, while the second argument "9" is a string.
   :feedback_c: The method expects a string and an int as actual arguments, not two ints.

   Based on the method header shown below, which method call is correct?

   .. code-block:: java

     public static void mystery(String s, int i)