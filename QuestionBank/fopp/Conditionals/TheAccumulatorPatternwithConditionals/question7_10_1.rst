.. mchoice:: question7_10_1
   :author: bmiller
   :difficulty: 2.0758075148
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: TheAccumulatorPatternwithConditionals
   :topics: Conditionals/TheAccumulatorPatternwithConditionals
   :from_source: T
   :answer_a: 2
   :answer_b: 5
   :answer_c: 0
   :answer_d: There is an error in the code so it cannot run.
   :correct: b
   :feedback_a: Though only two of the letters in the list are found, we count them each time they appear.
   :feedback_b: Yes, we add to x each time we come across a letter in the list.
   :feedback_c: Check again what the conditional is evaluating. The value of i will be a character in the string s, so what will happen in the if statement?
   :feedback_d: There are no errors in this code.
   :practice: T
   :pct_on_first: 0.7310481213
   :total_students_attempting: 1517
   :num_students_correct: 1503.0
   :mean_clicks_to_correct: 1.4258150366

   What is printed by the following statements?
   
   .. code-block:: python
   
     s = "We are learning!"
     x = 0
     for i in s:
         if i in ['a', 'b', 'c', 'd', 'e']:
             x += 1
     print(x)