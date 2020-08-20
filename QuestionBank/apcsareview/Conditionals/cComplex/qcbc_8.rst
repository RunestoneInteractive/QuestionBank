.. mchoice:: qcbc_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cComplex
   :topics: Conditionals/cComplex
   :from_source: T
   :answer_a: first case
   :answer_b: second case
   :correct: b
   :feedback_a: This will print if both of the conditions are true, but the second is not.
   :feedback_b: This will print if either of the conditions are false and the second one is (6 / 3 == 2).

   What is printed when the following code executes and x has been set to 3 and y has been set to 6?

   .. code-block:: java

     if (x > 0 && (y / x) == 3) System.out.println("first case");
     else System.out.println("second case");