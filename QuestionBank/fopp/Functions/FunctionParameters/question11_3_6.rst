.. mchoice:: question11_3_6
   :author: bmiller
   :difficulty: 1.941475827
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionParameters
   :topics: Functions/FunctionParameters
   :from_source: T
   :answer_a: Hello
   :answer_b: Goodbye
   :answer_c: s1
   :answer_d: s2
   :correct: b
   :feedback_a: "Hello" is shorter than "Goodbye"
   :feedback_b: "Goodbye" is longer than "Hello"
   :feedback_c: s1 is a variable name; its value would print out, not the variable name.
   :feedback_d: s2 is a variable name; its value would print out, not the variable name.
   :practice: T
   :pct_on_first: 0.7646310433
   :total_students_attempting: 1572
   :num_students_correct: 1566.0
   :mean_clicks_to_correct: 1.319284802

   What output will the following code produce?
   
   .. code-block:: python
   
      def cyu(s1, s2):
         if len(s1) > len(s2):
            print(s1)
         else:
            print(s2)
   
      cyu("Hello", "Goodbye")