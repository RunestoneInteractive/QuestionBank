.. mchoice:: question11_8_3
   :author: bmiller
   :difficulty: 2.319652723
   :basecourse: fopp
   :chapter: Functions
   :subchapter: GlobalVariables
   :topics: Functions/GlobalVariables
   :from_source: T
   :answer_a: Yes, and there is no reason not to.
   :answer_b: Yes, but it is considered bad form.
   :answer_c: No, it will cause an error.
   :correct: b
   :feedback_a: While there is no problem as far as Python is concerned, it is generally considered bad style because of the potential for the programmer to get confused.
   :feedback_b: it is generally considered bad style because of the potential for the programmer to get confused.  If you must use global variables (also generally bad form) make sure they have unique names.
   :feedback_c: Python manages global and local scope separately and has clear rules for how to handle variables with the same name in different scopes, so this will not cause a Python error.
   :pct_on_first: 0.6700868193
   :total_students_attempting: 1267
   :num_students_correct: 1253.0
   :mean_clicks_to_correct: 1.3926576217

   Can you use the same name for a local variable as a global variable?