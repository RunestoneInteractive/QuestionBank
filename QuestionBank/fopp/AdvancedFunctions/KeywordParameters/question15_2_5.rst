.. mchoice:: question15_2_5
   :author: bmiller
   :difficulty: 2.3366834171
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: KeywordParameters
   :topics: AdvancedFunctions/KeywordParameters
   :from_source: T
   :answer_a: 'first!' she yelled. 'Come here, first! f_one, f_two, and f_three are here!'
   :answer_b: 'Alexey!' she yelled. 'Come here, Alexey! Catalina, Misuki, and Pablo are here!'
   :answer_c: 'Catalina!' she yelled. 'Come here, Catalina! Alexey, Misuki, and Pablo are here!'
   :answer_d: There is an error. You cannot repeatedly use the keyword parameters.
   :correct: c
   :feedback_a: Remember, the values inside of {} are variable names. The values of the variables will be used.
   :feedback_b: Look again at what value is set to the variable first.
   :feedback_c: Yes, the keyword parameters will determine the order of the strings.
   :feedback_d: This is not an error, you can do that in Python!
   :practice: T
   :pct_on_first: 0.6658291457
   :total_students_attempting: 398
   :num_students_correct: 394.0
   :mean_clicks_to_correct: 1.4873096447

   What value will be printed below?
   
   .. code-block:: python
   
      names = ["Alexey", "Catalina", "Misuki", "Pablo"]
      print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))