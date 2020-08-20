.. mchoice:: 13_1_1_invoice_neg
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPStringDecisions
   :subchapter: decisionStrings
   :topics: CSPStringDecisions/decisionStrings
   :from_source: T
   :answer_a: You ordered 1 item
   :answer_b: Your ordered -1 items
   :answer_c: Nothing will be printed.
   :answer_d: You will get an error message that message is not defined.
   :correct: d
   :feedback_a: This line will only print when the numer of items is 1.
   :feedback_b: This line will print whenever the number of items is greater than 1.
   :feedback_c: If numItems is negative neither of the if's will be true so the variable message will not be created.
   :feedback_d: The variable message won't be created if the number of items is less than 1, so trying to print the value of message will cause an error.

   What will be printed if numItems = -1?