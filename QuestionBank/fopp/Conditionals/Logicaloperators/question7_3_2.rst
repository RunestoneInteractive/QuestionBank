.. mchoice:: question7_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Logicaloperators
   :topics: Conditionals/Logicaloperators
   :from_source: T
   :practice: T
   :multiple_answers: 
   :answer_a: Option A
   :answer_b: Option B
   :correct: a
   :feedback_a: Correct! The comparison yesno[0] == 'Y' will crash if yesno is an empty string.
   :feedback_b: Incorrect. If len(yesno) > 0 is False, the potentially unsafe comparison yesno[0] == 'Y' will not be evaluated.
   :pct_on_first: 0.624
   :total_students_attempting: 125
   :num_students_correct: 122.0
   :mean_clicks_to_correct: 1.4672131148

   Which of the following may result in a crash at runtime if the user presses Enter without typing a response?
   
   Option A) ::
   
      yesno = input('Enter Yes or No:')
      if yesno[0] == 'Y' and len(yesno) > 0:
         print('Yes!')
   
   Option B) ::
   
      yesno = input('Enter Yes or No:')
      if len(yesno) > 0 and yesno[0] == 'Y':
         print('Yes!')