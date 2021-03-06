.. mchoice:: question11_4_1
   :author: bmiller
   :difficulty: 2.4803986711
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: You should never use a print statement in a function definition.
   :answer_b: You should not have any statements in a function after the return statement.  Once the function gets to the return statement it will immediately stop executing the function.
   :answer_c: You must calculate the value of x+y+z before you return it.
   :answer_d: A function cannot return a number.
   :correct: b
   :feedback_a: Although you should not mistake print for return, you may include print statements inside your functions.
   :feedback_b: This is a very common mistake so be sure to watch out for it when you write your code!
   :feedback_c: Python will automatically calculate the value x+y+z and then return it in the statement as it is written
   :feedback_d: Functions can return any legal data, including (but not limited to) numbers, strings, lists, dictionaries, etc.
   :practice: T
   :pct_on_first: 0.6299003322
   :total_students_attempting: 1505
   :num_students_correct: 1496.0
   :mean_clicks_to_correct: 1.550802139

   What is wrong with the following function definition:
   
   .. code-block:: python
   
     def addEm(x, y, z):
         return x+y+z
         print('the answer is', x+y+z)