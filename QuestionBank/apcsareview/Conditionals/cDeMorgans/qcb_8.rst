.. mchoice:: qcb_8
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cDeMorgans
   :topics: Conditionals/cDeMorgans
   :from_source: F
   :answer_a: first case
   :answer_b: second case
   :correct: b
   :feedback_a: This will be printed if x is greater or equal to 3 and y is less than or equal to 2.  The first part is true but the second is false.  Since the statements are joined by an and the complex conditional is false.
   :feedback_b: This will be printed if x is less than 3 or y is greater than 2.  In this case the first will be false, but the second true so since the statements are joined with an or the complex conditional is true.

   What is printed when the following code executes and x equals 4 and y equals 3?

   .. code-block:: java

     if (!(x < 3 || y > 2)) System.out.println("first case");
     else System.out.println("second case");