.. mchoice:: question7_10_2
   :author: bmiller
   :difficulty: 2.8726790451
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: TheAccumulatorPatternwithConditionals
   :topics: Conditionals/TheAccumulatorPatternwithConditionals
   :from_source: T
   :answer_a: 10
   :answer_b: 1
   :answer_c: 0
   :answer_d: There is an error in the code so it cannot run.
   :correct: c
   :feedback_a: Not quite. What is the conditional checking?
   :feedback_b: min_value was set to a number that was smaller than any of the numbers in the list, so it was never updated in the for loop.
   :feedback_c: Yes, min_value was set to a number that was smaller than any of the numbers in the list, so it was never updated in the for loop.
   :feedback_d: The code does not have an error that would prevent it from running.
   :practice: T
   :pct_on_first: 0.5318302387
   :total_students_attempting: 1508
   :num_students_correct: 1496.0
   :mean_clicks_to_correct: 1.7292780749

   What is printed by the following statements?
   
   .. code-block:: python
   
     list= [5, 2, 1, 4, 9, 10]
     min_value = 0
     for item in list:
        if item < min_value:
            min_value = item
     print(min_value)