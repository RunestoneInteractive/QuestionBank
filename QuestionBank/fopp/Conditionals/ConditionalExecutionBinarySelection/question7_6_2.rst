.. mchoice:: question7_6_2
   :author: bmiller
   :difficulty: 1.4904632153
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: ConditionalExecutionBinarySelection
   :topics: Conditionals/ConditionalExecutionBinarySelection
   :from_source: T
   :answer_a: TRUE
   :answer_b: FALSE
   :answer_c: TRUE on one line and FALSE on the next
   :answer_d: Nothing will be printed
   :correct: b
   :feedback_a: TRUE is printed by the if-block, which only executes if the conditional (in this case, 4+5 == 10) is true.  In this case 5+4 is not equal to 10.
   :feedback_b: Since 4+5==10 evaluates to False, Python will skip over the if block and execute the statement in the else block.
   :feedback_c: Python would never print both TRUE and FALSE because it will only execute one of the if-block or the else-block, but not both.
   :feedback_d: Python will always execute either the if-block (if the condition is true) or the else-block (if the condition is false).  It would never skip over both blocks.
   :practice: T
   :pct_on_first: 0.8773841962
   :total_students_attempting: 1835
   :num_students_correct: 1826.0
   :mean_clicks_to_correct: 1.1944140197

   What does the following code print? (choose from output a, b, c or nothing)
   
   .. code-block:: python
   
     if (4 + 5 == 10):
         print("TRUE")
     else:
         print("FALSE")