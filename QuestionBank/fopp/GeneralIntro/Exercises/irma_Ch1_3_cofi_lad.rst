.. mchoice:: irma_Ch1_3_cofi_lad
        :author: Lynda Danielson
        :difficulty: 1.7272727273
        :basecourse: fopp
        :chapter: GeneralIntro
        :subchapter: Exercises
        :topics: GeneralIntro/Exercises
        :from_source: F
        :random: 
        :correct: b
        :answer_a: Line 1
        :answer_b: Line 2
        :answer_c: Line 3
        :answer_d: Line 5
        :feedback_a: Oh no. The value of m doesn't need changes since it is not involved in the division in Line 4.
        :feedback_b: Correct! Namely you can change the value of a to be anything but a 0, and the error in line 4 will be avoided. Well done!
        :feedback_c: Oh no. The value of b doesn't need changes since it is being divided.
        :feedback_d: Oh no. Line 5 is after the problematic line 4 and even if you fix it, the error will still be in line 4. You need to change the code AT or BEFORE line 4 in order to fix it.
        :pct_on_first: 0.8181818182
        :total_students_attempting: 22
        :num_students_correct: 22.0
        :mean_clicks_to_correct: 1.3636363636

        Consider the following program (you read line by line, top to bottom):
        
        .. code-block:: python
        
         line 1: m = 3
         line 2: a = 0
         line 3: b = 10
         line 4: c = b / a
         line 5: d = c + 3
        
        But oops, you realize that in line 4 you cannot divide the value of `b` by 0 (not allowed in math). 
        Which line of code will you need to change in order to successfully divide `b` by something that doesn't have the value of 0?