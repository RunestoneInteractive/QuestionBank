.. mchoice:: qve_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: T
   :practice: T
   :answer_a: 24
   :answer_b: 14
   :answer_c: This will give a compile time error.
   :answer_d: 16
   :correct: d
   :feedback_a: This would be true if it was System.out.println(((2 + 3) * 5) - 1), but without the parentheses the multiplication is done first.
   :feedback_b: This would be true if it was System.out.println(2 + (3 * (5 - 1))), but without the parentheses the multiplication is done first and the addition and subtraction are handled from left to right.
   :feedback_c: This will compile and run.  Try it in DrJava.  Look up operator precedence in Java.
   :feedback_d: The multiplication is done first (3 * 5 = 15) and then the addition (2 + 15 = 17) and finally the subtraction (17 - 1 = 16).
   :pct_on_first: 0.8739952205
   :total_students_attempting: 4603
   :num_students_correct: 4589.0
   :mean_clicks_to_correct: 1.1956853345

   What does the following code print?
   
   .. code-block:: java
   
    System.out.println(2 + 3 * 5 - 1);