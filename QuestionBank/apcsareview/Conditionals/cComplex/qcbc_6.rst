.. mchoice:: qcbc_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cComplex
   :topics: Conditionals/cComplex
   :from_source: T
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't divide by zero.
   :correct: c
   :feedback_a: This will print if either of the two conditions are true.  The first isn't true but the second will cause an error.
   :feedback_b: This will print if both of the conditions are false.  But, an error will occur when testing the second condition.
   :feedback_c: The first condition will be false so the second one will be executed and lead to an error since you can't divide by zero.

   What is printed when the following code executes and x has been set to zero?  Notice that it is now a logical or rather than an and.

   .. code-block:: java

     if (x > 0 || (y / x) == 3) System.out.println("first case");
     else System.out.println("second case");