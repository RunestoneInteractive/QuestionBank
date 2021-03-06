.. mchoice:: mc5o
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Functions
   :subchapter: TheAccumulatorPattern
   :topics: Functions/TheAccumulatorPattern
   :from_source: None
   :answer_a: The square function will return x instead of x * x
   :answer_b: The square function will cause an error
   :answer_c: The square function will work as expected and return x * x
   :answer_d: The square function will return 0 instead of x * x
   :correct: a
   :feedback_a: The variable runningtotal will be reset to 0 each time through the loop.   However because this assignment happens as the first instruction, the next instruction in the loop will set it back to x.   When the loop finishes, it will have the value x, which is what is returned.
   :feedback_b: Assignment statements are perfectly legal inside loops and will not cause an error.
   :feedback_c: By putting the statement that sets runningtotal to 0 inside the loop, that statement gets executed every time through the loop, instead of once before the loop begins.  The result is that runningtotal is 'cleared' (reset to 0) each time through the loop.
   :feedback_d: The line runningtotal = 0 is the first line in the for loop, but immediately after this line, the line runningtotal = runningtotal + x will execute, giving runningtotal a non-zero value  (assuming x is non-zero).

   Consider the following code:

   .. code-block:: python

     def square(x):
         runningtotal = 0
         for counter in range(x):
             runningtotal = runningtotal + x
         return runningtotal

   What happens if you put the initialization of runningtotal (the
   line runningtotal = 0) inside the for loop as the first
   instruction in the loop?