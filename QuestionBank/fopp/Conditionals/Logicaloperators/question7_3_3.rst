.. mchoice:: question7_3_3
   :author: bmiller
   :difficulty: 2.5172413793
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Logicaloperators
   :topics: Conditionals/Logicaloperators
   :from_source: T
   :practice: T
   :answer_a: Option A
   :answer_b: Option B
   :answer_c: Option C
   :answer_d: Option D
   :correct: b
   :feedback_a: Incorrect. The comparison yesno[0] == 'Y' will crash if yesno is an empty string.
   :feedback_b: Correct! Use the and operator to join nested if statements into a single statement, with the first if condition on the left-hand side.
   :feedback_c: Incorrect. The comparison yesno[0] == 'Y' will crash if yesno is an empty string.
   :feedback_d: Incorrect. The comparison yesno[0] == 'Y' will crash if yesno is an empty string.
   :pct_on_first: 0.6206896552
   :total_students_attempting: 116
   :num_students_correct: 115.0
   :mean_clicks_to_correct: 1.7043478261

   Consider the following fragment containing a nested ``if`` statement to prevent a crash in the event
   the user enters an empty response for ``yesno``::
   
      yesno = input('Enter Yes or No:')
      if len(yesno) > 0:
         if yesno[0] == 'Y':
            print('Yes!')
   
   Which of the following is the correct way to combine the nested ``if`` into a single ``if`` statement that executes
   identically to the nested ``if`` statements?
   
   Option A) ::
   
      if yesno[0] == 'Y' and len(yesno) > 0:
         print('Yes!')
   
   Option B) ::
   
      if len(yesno) > 0 and yesno[0] == 'Y':
         print('Yes!')
   
   Option C) ::
   
      if yesno[0] == 'Y' or len(yesno) > 0:
         print('Yes!')
   
   Option D) ::
   
      if len(yesno) > 0 or yesno[0] == 'Y':
         print('Yes!')