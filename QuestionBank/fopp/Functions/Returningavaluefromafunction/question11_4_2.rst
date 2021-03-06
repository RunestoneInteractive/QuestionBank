.. mchoice:: question11_4_2
   :author: bmiller
   :difficulty: 2.9800664452
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: The value None
   :answer_b: The value of x+y+z
   :answer_c: The string 'x+y+z'
   :correct: a
   :feedback_a: We have accidentally used print where we mean return.  Therefore, the function will return the value None by default.  This is a VERY COMMON mistake so watch out!  This mistake is also particularly difficult to find because when you run the function the output looks the same.  It is not until you try to assign its value to a variable that you can notice a difference.
   :feedback_b: Careful!  This is a very common mistake.  Here we have printed the value x+y+z but we have not returned it.  To return a value we MUST use the return keyword.
   :feedback_c: x+y+z calculates a number (assuming x+y+z are numbers) which represents the sum of the values x, y and z.
   :practice: T
   :pct_on_first: 0.5049833887
   :total_students_attempting: 1505
   :num_students_correct: 1496.0
   :mean_clicks_to_correct: 1.8128342246

   What will the following function return?
   
   .. code-block:: python
   
    def addEm(x, y, z):
        print(x+y+z)