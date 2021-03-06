.. mchoice:: question11_4_7
   :author: bmiller
   :difficulty: 3.4553633218
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: 3
   :answer_b: 2
   :answer_c: None
   :correct: b
   :feedback_a: The function gets to a return statement after 2 lines are printed, so the third print statement will not run.
   :feedback_b: Yes! Two printed lines, and then the function body execution reaches a return statement.
   :feedback_c: The function returns an integer value! However, this code does not print out the result of the function invocation, so you can't see it (print is for people). The only lines you see printed are the ones that occur in the print statements before the return statement.
   :practice: T
   :pct_on_first: 0.3861591696
   :total_students_attempting: 1445
   :num_students_correct: 1436.0
   :mean_clicks_to_correct: 1.7778551532

   How many lines will the following code print?
   
   .. code-block:: python
   
       def show_me_numbers(list_of_ints):
           print(10)
           print("Next we'll accumulate the sum")
           accum = 0
           for num in list_of_ints:
               accum = accum + num
           return accum
           print("All done with accumulation!")
   
       show_me_numbers([4,2,3])