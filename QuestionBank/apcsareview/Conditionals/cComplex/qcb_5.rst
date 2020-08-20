.. mchoice:: qcb_5
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cComplex
   :topics: Conditionals/cComplex
   :from_source: F
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't divide by zero.
   :correct: b
   :feedback_a: This will only print if x is greater than 0 and it is not.
   :feedback_b: This will print if x is less than or equal to zero or if y divided by x is not equal to 3.
   :feedback_c: Since the first condition if false when x is equal to zero the second condition won't execute.  Execution moves to the else.

   What is printed when the following code executes and x has been set to zero?

   .. code-block:: java

     if (x > 0 && (y / x) == 3) System.out.println("first case");
     else System.out.println("second case");