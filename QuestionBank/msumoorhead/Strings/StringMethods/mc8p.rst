.. mchoice:: mc8p
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: StringMethods
   :topics: Strings/StringMethods
   :from_source: None
   :answer_a: 2.34567 2.34567 2.34567
   :answer_b: 2.3 2.34 2.34567
   :answer_c: 2.3 2.35 2.3456700
   :correct: c
   :feedback_a: The numbers before the f in the braces give the number of digits to display after the decimal point.
   :feedback_b: Close, but round to the number of digits and display the full number of digits specified.
   :feedback_c: Yes, correct number of digits with rounding!


   What is printed by the following statements?

   .. code-block:: python

       v = 2.34567
       print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))