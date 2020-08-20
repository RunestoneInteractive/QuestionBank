.. mchoice:: mc1l
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: GeneralIntro
   :subchapter: RuntimeErrors
   :topics: GeneralIntro/RuntimeErrors
   :from_source: None
   :answer_a: Attempting to divide by 0.
   :answer_b: Forgetting a closing parenthesis character ")" where one is required.
   :answer_c: Dividing the gallons consumed by the miles driven when calculating the MPG of a vehicle.
   :correct: a
   :feedback_a: Python cannot reliably tell if you are trying to divide by 0 until it is executing your program (e.g., you might be asking the user for a value and then dividing by that value - you cannot know what value the user will enter before you run the program).
   :feedback_b: This is a problem with the formal structure of the program.  Python knows when there is a missing parenthesis by looking at the code without running it.
   :feedback_c: This will produce the wrong answer, but Python will not consider it an error at all.  The programmer is the one who must understand that the answer produced is wrong.

   Which of the following is a run-time error?