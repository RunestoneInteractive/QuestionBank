.. mchoice:: question1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: Functions
   :subchapter: DefiningFunctions
   :topics: Functions/DefiningFunctions
   :from_source: T
   :answer_a: The "&" forces variables to change in the global scope, resulting in the two variables not exclusively changing inside of the function.
   :answer_b: The "&" passes the location where the two variables are stored, resulting in the two variables switching memory references.
   :answer_c: The "&" in this function is incorrectly used, resulting in an overlapping memory reference.
   :answer_d: None of the above
   :correct: b
   :feedback_a: No, "&" has nothing to do with altering integers in the global scope.
   :feedback_b: Correct!
   :feedback_c: No, the use of "&" here is correct. Read over the active code 4 example earlier in the section.
   :feedback_d: No, one of the above is definitely true.

   Why does adding the "&" to parameters in the **func** function cause the output to be a different result?