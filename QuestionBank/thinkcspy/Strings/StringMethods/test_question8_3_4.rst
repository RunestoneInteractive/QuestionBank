.. mchoice:: test_question8_3_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: StringMethods
   :topics: Strings/StringMethods
   :from_source: T
   :practice: T
   :answer_a: 2.34567 2.34567 2.34567
   :answer_b: 2.3 2.34 2.34567
   :answer_c: 2.3 2.35 2.3456700
   :correct: c
   :feedback_a: The numbers before the f in the braces give the number of digits to display after the decimal point.
   :feedback_b: Close, but round to the number of digits and display the full number of digits specified.
   :feedback_c: Yes, correct number of digits with rounding!
   :pct_on_first: 0.4853116134
   :total_students_attempting: 10927
   :num_students_correct: 10869.0
   :mean_clicks_to_correct: 1.6673107002

   
   What is printed by the following statements?
   
   .. code-block:: python
   
       v = 2.34567
       print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))