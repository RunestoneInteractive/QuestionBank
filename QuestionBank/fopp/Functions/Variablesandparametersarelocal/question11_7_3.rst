.. mchoice:: question11_7_3
   :author: bmiller
   :difficulty: 2.4606569901
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Variablesandparametersarelocal
   :topics: Functions/Variablesandparametersarelocal
   :from_source: T
   :answer_a: 33
   :answer_b: 12
   :answer_c: There is an error in the code.
   :correct: c
   :feedback_a: Incorrect, look again at what is happening in producing.
   :feedback_b: Incorrect, look again at what is happening in producing.
   :feedback_c: Yes! There is an error because we reference y in the producing function, but it was defined in adding. Because y is a local variable, we can't use it in both functions without initializing it in both. If we initialized y as 3 in both though, the answer would be 33.
   :practice: T
   :pct_on_first: 0.6348357525
   :total_students_attempting: 1309
   :num_students_correct: 1293.0
   :mean_clicks_to_correct: 1.6635730858

   What is the result of the following code?
   
   .. sourcecode:: python
   
     def adding(x):
         y = 3
         z = y + x + x
         return z
   
     def producing(x):
         z = x * y
         return z
   
     print(producing(adding(4)))