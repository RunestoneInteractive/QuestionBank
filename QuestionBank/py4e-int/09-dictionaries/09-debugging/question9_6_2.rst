.. mchoice:: question9_6_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-debugging
   :topics: 09-dictionaries/09-debugging
   :from_source: T
   :practice: T
   :answer_a: Python is performing a string concatenation and not integer addition
   :answer_b: There is nothing wrong with this code
   :answer_c: There is a parenthesis that was never closed
   :correct: a
   :feedback_a: Correct! The input function returns a string not an integer. For this to be correct, you would need to initialize input as an integer like so: int(input(...))
   :feedback_b: Try again!
   :feedback_c: Try again!

   What error (if any) appears when the following code is run?

   .. activecode:: example9_6_2

      current_time = input("What is the current time in hours?")
      wait_time = input("How many hours do you want to wait?")

      print(current_time)
      print(wait_time)

      final_time = current_time + wait_time
      print(final_time)