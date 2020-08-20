.. mchoice:: 13_1_2_invoice_else
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPStringDecisions
   :subchapter: decisionStrings
   :topics: CSPStringDecisions/decisionStrings
   :from_source: T
   :answer_a: You ordered 1 item
   :answer_b: Your ordered -1 items
   :answer_c: Nothing will be printed.
   :answer_d: You will get an error message that message is not defined.
   :correct: b
   :feedback_a: This line will still only print when the numer of items is 1.
   :feedback_b: This line will print whenever the number of items was not equal to 1 when you change the second if to an else.
   :feedback_c: If numItems is negative neither of the if's will be true so the variable message will not be created.
   :feedback_d: The variable message won't be created if the number of items is less than 1, so trying to print the value of message will cause an error.
   :pct_on_first: 0.5485564304
   :total_students_attempting: 762
   :num_students_correct: 760.0
   :mean_clicks_to_correct: 1.8302631579

   What will be printed if you change the second if to an else and set numItems = -1?